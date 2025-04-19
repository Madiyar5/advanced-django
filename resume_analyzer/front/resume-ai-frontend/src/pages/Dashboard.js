import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Dashboard = () => {
  const [userData, setUserData] = useState(null);
  const [resumeFile, setResumeFile] = useState(null);
  const [uploadResult, setUploadResult] = useState(null);
  const [resumeList, setResumeList] = useState([]);

  const accessToken = localStorage.getItem('access_token');

  useEffect(() => {
    axios.get('http://localhost:8000/api/user/', {
      headers: { Authorization: `Bearer ${accessToken}` },
    })
      .then(res => setUserData(res.data))
      .catch(err => console.error(err));
  }, [accessToken]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/resumes/info', {
      headers: { Authorization: `Bearer ${accessToken}` },
    })
      .then(res => setResumeList(res.data))
      .catch(err => console.error(err));
  }, [accessToken, uploadResult]);

  const handleFileChange = (e) => setResumeFile(e.target.files[0]);

  const handleUpload = async () => {
    if (!resumeFile) return;
    const formData = new FormData();
    formData.append('file', resumeFile);

    try {
      const res = await axios.post('http://localhost:8000/api/resumes/upload/', formData, {
        headers: {
          Authorization: `Bearer ${accessToken}`,
          'Content-Type': 'multipart/form-data',
        },
      });
      setUploadResult(res.data);
      setResumeFile(null);
    } catch (err) {
      console.error('Upload error:', err);
    }
  };

  return (
    <div className="flex flex-col md:flex-row p-6 gap-6">
      {/* Левая колонка */}
      <div className="flex-1">
        <h1 className="text-3xl font-bold mb-6">Dashboard</h1>

        <div className="flex items-center gap-4 mb-6">
          <input type="file" onChange={handleFileChange} />
          <button
            onClick={handleUpload}
            className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
          >
            Upload Resume
          </button>
        </div>

        <h2 className="text-2xl font-semibold mb-4">Parsed Resumes</h2>

        {resumeList.length === 0 ? (
          <p className="text-gray-500">No resumes uploaded yet.</p>
        ) : (
          resumeList.map((resume, idx) => (
            <div key={idx} className="mb-6 p-5 border rounded-lg shadow bg-gray-50">
              {resume.filename && (
                <p className="font-semibold text-blue-800 mb-2">
                  Filename: <span className="font-normal">{resume.filename}</span>
                </p>
              )}
              {resume.skills && (
                <p><strong>Skills:</strong> {Array.isArray(resume.skills) ? resume.skills.join(', ') : resume.skills}</p>
              )}
              {resume.experience && (
                <div className="mt-2">
                  <strong>Experience:</strong>
                  <ul className="list-disc ml-6">
                    {Array.isArray(resume.experience)
                      ? resume.experience.map((item, i) => <li key={i}>{item}</li>)
                      : <li>{resume.experience}</li>}
                  </ul>
                </div>
              )}
              {resume.education && (
                <div className="mt-2">
                  <strong>Education:</strong>
                  <ul className="list-disc ml-6">
                    {Array.isArray(resume.education)
                      ? resume.education.map((item, i) => <li key={i}>{item}</li>)
                      : <li>{resume.education}</li>}
                  </ul>
                </div>
              )}
            </div>
          ))
        )}
      </div>

      {/* Правая колонка */}
      <div className="w-full md:w-80 bg-white border-l p-4 shadow-sm">
        <h2 className="text-2xl font-bold mb-4">Profile</h2>
        {userData ? (
          <>
            <p className="mb-4"><strong>Username:</strong> {userData.username}</p>
            <h3 className="text-lg font-semibold mb-2">Your Resumes</h3>
            {resumeList.length > 0 ? (
              <ul className="list-disc ml-5">
                {resumeList.map((resume, idx) => (
                  <li key={idx}>{resume.filename || `Resume #${idx + 1}`}</li>
                ))}
              </ul>
            ) : (
              <p className="text-gray-500">You haven't uploaded any resumes.</p>
            )}
          </>
        ) : (
          <p className="text-gray-500">Loading user info...</p>
        )}
      </div>
    </div>
  );
};

export default Dashboard;
