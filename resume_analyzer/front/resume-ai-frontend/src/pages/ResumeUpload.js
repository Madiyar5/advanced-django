import React, { useState } from "react";
import axios from "axios";

const ResumeUpload = () => {
  const [file, setFile] = useState(null);
  const [response, setResponse] = useState(null);

  const handleUpload = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("file", file);

    const token = localStorage.getItem("access");

    try {
      const res = await axios.post(
        "http://localhost:8000/api/resumes/upload/",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
            Authorization: `Bearer ${token}`,
          },
        }
      );
      setResponse(res.data);
    } catch (err) {
      alert("Ошибка загрузки");
      console.error(err);
    }
  };

  return (
    <div>
      <h2>Upload Resume</h2>
      <form onSubmit={handleUpload}>
        <input type="file" onChange={(e) => setFile(e.target.files[0])} />
        <button type="submit">Upload</button>
      </form>

      {response && (
        <div>
          <h3>AI Extracted Data</h3>
          <p><strong>Skills:</strong> {response.skills?.join(", ")}</p>
          <p><strong>Experience:</strong> {response.experience?.join(", ")}</p>
          <p><strong>Education:</strong> {response.education?.join(", ")}</p>
        </div>
      )}
    </div>
  );
};

export default ResumeUpload;
