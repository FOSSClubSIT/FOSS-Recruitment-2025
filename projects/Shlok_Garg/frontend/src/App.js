import React, { useState, useRef } from "react";
import "./App.css";
import axios from "axios";

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

const App = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [analysis, setAnalysis] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const fileInputRef = useRef(null);

  const handleFileSelect = (event) => {
    const file = event.target.files[0];
    if (file) {
      if (file.type !== "application/pdf") {
        setError("Please select a PDF file");
        return;
      }
      if (file.size > 15 * 1024 * 1024) {
        setError("File size must be less than 15MB");
        return;
      }
      setSelectedFile(file);
      setError("");
    }
  };

  const handleDragOver = (event) => {
    event.preventDefault();
  };

  const handleDrop = (event) => {
    event.preventDefault();
    const file = event.dataTransfer.files[0];
    if (file) {
      if (file.type !== "application/pdf") {
        setError("Please select a PDF file");
        return;
      }
      if (file.size > 15 * 1024 * 1024) {
        setError("File size must be less than 15MB");
        return;
      }
      setSelectedFile(file);
      setError("");
    }
  };

  const analyzeResume = async () => {
    if (!selectedFile) {
      setError("Please select a PDF file");
      return;
    }

    setLoading(true);
    setError("");
    setAnalysis(null);

    const formData = new FormData();
    formData.append("resume", selectedFile);

    try {
      const response = await axios.post(`${API}/analyze`, formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
        timeout: 90000, // 90 second timeout for enhanced models
      });
      setAnalysis(response.data);
    } catch (err) {
      console.error("Analysis error:", err);
      setError(
        err.response?.data?.detail || 
        "Failed to analyze resume. Please try again."
      );
    } finally {
      setLoading(false);
    }
  };

  const resetForm = () => {
    setSelectedFile(null);
    setAnalysis(null);
    setError("");
    if (fileInputRef.current) {
      fileInputRef.current.value = "";
    }
  };

  // Header component with improved design
  const Header = () => (
    <div className="bg-gradient-to-r from-indigo-600 via-blue-600 to-purple-600 text-white shadow-lg">
      <div className="container mx-auto px-4 py-8">
        <div className="text-center">
          <h1 className="text-4xl font-bold mb-2">
            ✨ AI Resume Analyzer
          </h1>
          <p className="text-xl opacity-90">
            Advanced AI-powered resume analysis and job matching
          </p>
          <div className="mt-4 flex justify-center space-x-8 text-sm opacity-80">
            <div className="flex items-center space-x-2">
              <span>🧠</span>
              <span>Advanced NLP Models</span>
            </div>
            <div className="flex items-center space-x-2">
              <span>🎯</span>
              <span>Smart Job Matching</span>
            </div>
            <div className="flex items-center space-x-2">
              <span>⚡</span>
              <span>Instant Analysis</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );

  const EntityBadge = ({ entities, title, color }) => (
    <div className="bg-white rounded-lg shadow-sm border p-4">
      <h4 className={`font-semibold mb-2 text-${color}-600`}>{title}</h4>
      <div className="flex flex-wrap gap-2">
        {entities.length > 0 ? (
          entities.map((entity, index) => (
            <span
              key={index}
              className={`px-3 py-1 bg-${color}-100 text-${color}-800 rounded-full text-sm font-medium`}
            >
              {entity}
            </span>
          ))
        ) : (
          <span className="text-gray-500 text-sm">None detected</span>
        )}
      </div>
    </div>
  );

  const JobProfileAnalysis = ({ profileData }) => {
    if (!profileData) return null;

    const getScoreColor = (score) => {
      if (score >= 80) return "text-green-600";
      if (score >= 60) return "text-yellow-600";
      return "text-red-600";
    };

    const getProgressColor = (score) => {
      if (score >= 80) return "bg-green-500";
      if (score >= 60) return "bg-yellow-500";
      return "bg-red-500";
    };

    return (
      <div className="bg-white rounded-xl shadow-lg p-6 mb-6">
        <div className="flex items-center justify-between mb-4">
          <h3 className="text-2xl font-bold text-gray-800">
            🎯 Job Profile Analysis
          </h3>
          <div className="text-right">
            <div className="text-sm text-gray-600">Detected Role</div>
            <div className="font-semibold text-blue-600">
              {profileData.detected_role}
            </div>
            <div className="text-xs text-gray-500">
              {Math.round(profileData.role_confidence * 100)}% confidence
            </div>
          </div>
        </div>

        {/* Overall Score */}
        <div className="mb-6">
          <div className="flex items-center justify-between mb-2">
            <span className="text-lg font-medium text-gray-700">Overall Score</span>
            <span className={`text-2xl font-bold ${getScoreColor(profileData.overall_score)}`}>
              {profileData.overall_score}/100
            </span>
          </div>
          <div className="w-full bg-gray-200 rounded-full h-3">
            <div
              className={`h-3 rounded-full transition-all duration-500 ${getProgressColor(profileData.overall_score)}`}
              style={{ width: `${profileData.overall_score}%` }}
            ></div>
          </div>
        </div>

        {/* Category Breakdown */}
        <div className="grid md:grid-cols-2 gap-4 mb-6">
          {Object.entries(profileData.category_scores).map(([category, data]) => (
            <div key={category} className="border border-gray-200 rounded-lg p-4">
              <div className="flex items-center justify-between mb-2">
                <span className="font-medium text-gray-700 capitalize">
                  {category.replace('_', ' ')}
                </span>
                <span className={`font-semibold ${getScoreColor(data.score)}`}>
                  {Math.round(data.score)}/100
                </span>
              </div>
              
              <div className="w-full bg-gray-200 rounded-full h-2 mb-3">
                <div
                  className={`h-2 rounded-full ${getProgressColor(data.score)}`}
                  style={{ width: `${data.score}%` }}
                ></div>
              </div>

              {/* Found Skills */}
              {data.found && data.found.length > 0 && (
                <div className="mb-2">
                  <div className="text-xs text-green-600 font-medium mb-1">✓ Found</div>
                  <div className="flex flex-wrap gap-1">
                    {data.found.slice(0, 5).map((item, idx) => (
                      <span
                        key={idx}
                        className="px-2 py-1 bg-green-100 text-green-800 rounded text-xs"
                      >
                        {item}
                      </span>
                    ))}
                    {data.found.length > 5 && (
                      <span className="px-2 py-1 bg-gray-100 text-gray-600 rounded text-xs">
                        +{data.found.length - 5} more
                      </span>
                    )}
                  </div>
                </div>
              )}

              {/* Missing Skills */}
              {data.missing && data.missing.length > 0 && (
                <div>
                  <div className="text-xs text-red-600 font-medium mb-1">⚠ Missing</div>
                  <div className="flex flex-wrap gap-1">
                    {data.missing.slice(0, 3).map((item, idx) => (
                      <span
                        key={idx}
                        className="px-2 py-1 bg-red-100 text-red-800 rounded text-xs"
                      >
                        {item}
                      </span>
                    ))}
                  </div>
                </div>
              )}
            </div>
          ))}
        </div>

        {/* Recommendations */}
        {profileData.recommendations && profileData.recommendations.length > 0 && (
          <div>
            <h4 className="font-bold mb-4 text-gray-800 flex items-center text-lg">
              💡 Smart Recommendations
            </h4>
            <div className="space-y-2">
              {profileData.recommendations.map((rec, index) => (
                <div
                  key={index}
                  className="flex items-start space-x-2 p-3 bg-blue-50 border-l-4 border-blue-400 rounded"
                >
                  <span className="text-blue-600 mt-0.5">•</span>
                  <span className="text-blue-800 text-sm">{rec}</span>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    );
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50">
      <Header />
      
      <div className="container mx-auto px-4 py-8">
        {/* Enhanced Upload Section */}
        <div className="bg-white rounded-xl shadow-lg p-8 mb-8">
          <div className="text-center mb-8">
            <h2 className="text-3xl font-bold text-gray-800 mb-2">
              Get Started with Your Resume Analysis
            </h2>
            <p className="text-gray-600">
              Upload your resume and let our AI provide comprehensive insights and analysis
            </p>
          </div>
          
          <div className="flex justify-center">
            {/* File Upload */}
            <div className="w-full max-w-md">
              <div className="flex items-center justify-center space-x-2 mb-6">
                <span className="text-3xl">📄</span>
                <h3 className="text-2xl font-bold text-gray-700">Upload Your Resume</h3>
              </div>
              <div
                className="border-2 border-dashed border-gray-300 rounded-xl p-16 text-center cursor-pointer hover:border-indigo-400 hover:bg-indigo-50 transition-all duration-300 group"
                onDragOver={handleDragOver}
                onDrop={handleDrop}
                onClick={() => fileInputRef.current?.click()}
              >
                {selectedFile ? (
                  <div className="space-y-6">
                    <div className="text-8xl">📄</div>
                    <div>
                      <p className="font-bold text-gray-800 text-xl">{selectedFile.name}</p>
                      <p className="text-gray-600 text-lg mt-2">
                        {(selectedFile.size / 1024 / 1024).toFixed(2)} MB
                      </p>
                    </div>
                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        resetForm();
                      }}
                      className="px-6 py-3 bg-red-500 hover:bg-red-600 text-white rounded-lg font-semibold transition-colors"
                    >
                      Remove File
                    </button>
                  </div>
                ) : (
                  <div className="space-y-6 group-hover:scale-105 transition-transform">
                    <div className="text-8xl">📁</div>
                    <div>
                      <p className="font-bold text-gray-700 text-2xl">
                        Drop your PDF here
                      </p>
                      <p className="text-gray-500 text-xl mt-3">
                        or click to browse files
                      </p>
                      <p className="text-sm text-gray-400 mt-4">Maximum file size: 15MB</p>
                    </div>
                  </div>
                )}
                <input
                  ref={fileInputRef}
                  type="file"
                  accept=".pdf"
                  onChange={handleFileSelect}
                  className="hidden"
                />
              </div>
            </div>
          </div>

          {/* Action Buttons */}
          <div className="flex justify-center space-x-6 mt-10">
            <button
              onClick={analyzeResume}
              disabled={!selectedFile || loading}
              className={`px-12 py-4 rounded-xl font-bold text-lg text-white transition-all duration-300 transform ${
                selectedFile && !loading
                  ? "bg-gradient-to-r from-indigo-600 via-blue-600 to-purple-600 hover:from-indigo-700 hover:via-blue-700 hover:to-purple-700 shadow-xl hover:shadow-2xl hover:scale-105"
                  : "bg-gray-400 cursor-not-allowed"
              }`}
            >
              {loading ? (
                <div className="flex items-center space-x-3">
                  <div className="animate-spin h-6 w-6 border-3 border-white border-t-transparent rounded-full"></div>
                  <span>Analyzing with AI...</span>
                </div>
              ) : (
                <div className="flex items-center space-x-3">
                  <span className="text-xl">�</span>
                  <span>Analyze Resume</span>
                </div>
              )}
            </button>

            {(selectedFile || analysis) && (
              <button
                onClick={resetForm}
                className="px-8 py-4 bg-gray-600 hover:bg-gray-700 text-white rounded-xl font-bold text-lg transition-all duration-300 transform hover:scale-105"
              >
                <div className="flex items-center space-x-2">
                  <span>🔄</span>
                  <span>Reset</span>
                </div>
              </button>
            )}
          </div>
        </div>

        {/* Error Display */}
        {error && (
          <div className="bg-gradient-to-r from-red-50 to-pink-50 border-2 border-red-200 rounded-xl p-6 mb-8 shadow-lg">
            <div className="flex items-start space-x-3">
              <span className="text-red-600 text-2xl">⚠️</span>
              <div>
                <h4 className="text-red-800 font-bold text-lg mb-1">Something went wrong</h4>
                <p className="text-red-700">{error}</p>
              </div>
            </div>
          </div>
        )}

        {/* Enhanced Analysis Results */}
        {analysis && (
          <div className="bg-gradient-to-br from-gray-50 to-white rounded-xl shadow-xl p-8">
          <div className="text-center mb-8">
            <h3 className="text-3xl font-bold text-gray-800 mb-2">
              📊 Analysis Results
            </h3>
            <p className="text-gray-600 text-lg">
              Comprehensive AI-powered insights about your resume
            </p>
          </div>

            {/* Job Profile Analysis */}
            <JobProfileAnalysis profileData={analysis.job_profile_analysis} />

            {/* Enhanced Entities Section */}
            <div className="bg-white rounded-xl shadow-lg p-8 mt-8">
              <h3 className="text-2xl font-bold text-gray-800 mb-6 text-center">
                🧠 AI Entity Recognition
              </h3>
              <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
                <EntityBadge 
                  entities={analysis.entities.names} 
                  title="👤 Names" 
                  color="blue" 
                />
                <EntityBadge 
                  entities={analysis.entities.organizations} 
                  title="🏢 Organizations" 
                  color="purple" 
                />
                <EntityBadge 
                  entities={analysis.entities.skills} 
                  title="⚡ Technical Skills" 
                  color="green" 
                />
                <EntityBadge 
                  entities={analysis.entities.locations} 
                  title="📍 Locations" 
                  color="red" 
                />
              </div>
            </div>

            {/* Resume Preview */}
            <div className="bg-white rounded-xl shadow-lg p-8 mt-8">
              <h3 className="text-2xl font-bold text-gray-800 mb-4 text-center">
                📄 Resume Content
              </h3>
              <div className="bg-gradient-to-br from-gray-50 to-gray-100 rounded-xl p-6 max-h-80 overflow-y-auto">
                <p className="text-gray-700 leading-relaxed whitespace-pre-line">
                  {analysis.resume_text}
                </p>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default App;
