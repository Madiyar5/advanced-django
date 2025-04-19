from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import ResumeSerializer
from .models import Resume
from .utils import extract_resume_text
from .ai_utils import extract_skills, extract_experience, extract_education

class ResumeUploadView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ResumeSerializer(data=request.data)
        if serializer.is_valid():
            resume = serializer.save(user=request.user)
            #parsing file
            text = extract_resume_text(resume.file.path)

            #AI using
            skills = extract_skills(text)
            experience = extract_experience(text)
            education = extract_education(text)

            #saving
            resume.skills = ", ".join(skills)
            resume.experience = "\n".join(experience)
            resume.education = "\n".join(education)
            resume.save()
            return Response({
                "resume": serializer.data,
                "skills": skills,
                "experience": experience,
                "education": education
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        return Response({"message": "Resume endpoint working"})

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Resume
from .serializers import ResumeSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_resumes(request):
    resumes = Resume.objects.filter(user=request.user).order_by('-uploaded_at')
    serializer = ResumeSerializer(resumes, many=True)
    return Response(serializer.data)
