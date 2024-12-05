import React, { useState, useEffect } from "react";
import { useSearchParams, useNavigate } from "react-router-dom";
import axios from "axios";
import "./Result.css";

// Import child components
import GlassdoorRating from "./GlassdoorRating";
import CapterraRating from "./CapterraRating";
import EmployeeReviews from "./EmployeeReviews";
import GoogleNews from "./GoogleNews";
import PressRelease from "./PressRelease";
import Patents from "./Patents";

const Result = () => {
  const [companyData, setCompanyData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Extract query parameter (company name) from the URL
  const [searchParams] = useSearchParams();
  const companyName = searchParams.get("query");

  const navigate = useNavigate();

  useEffect(() => {
    if (!companyData && companyName) {
      // Fetch data from the backend
      const fetchData = async () => {
        try {
          const response = await axios.get(
            `http://127.0.0.1:8000/search?company_name=${encodeURIComponent(companyName)}`
          );
          setCompanyData(response.data); // Ensure "news" is part of the data
        } catch (err) {
          setError("Failed to fetch data. Please try again later.");
        } finally {
          setLoading(false);
        }
      };
      fetchData();
    } else {
      setError("No company name provided.");
      setLoading(false);
    }
  }, [companyName]);

  if (loading) {
    return <div className="loading-message">Loading company insights...</div>;
  }

  if (error) {
    return (
      <div className="error-message">
        <p>{error}</p>
        <button className="back-button" onClick={() => navigate("/")}>
          Go Back to Home
        </button>
      </div>
    );
  }

  return (
    <div className="result-page">
      {/* Navigation Back to Homepage */}
      <button className="back-button" onClick={() => navigate("/")}>
        Go Back to Home
      </button>

      {/* Title and Subtitle */}
      <div className="result-header">
        <h1 className="company-title">{companyData.company_name || "Company Insights"}</h1>
        <p className="company-subtext">
          We provide comprehensive company details and metrics from various public sources.
        </p>
      </div>

      {/* Horizontal Components */}
      <div className="horizontal-components">
        <GlassdoorRating data={companyData.glassdoor} />
        <CapterraRating data={companyData.capterra} />
      </div>

      {/* Employee Reviews Component */}
      <EmployeeReviews data={companyData.reviews} />

      {/* Google News Component */}
      <GoogleNews data={companyData.news.slice(0, 10)} /> {/* Display only the first 10 results */}

      {/* Press Release Component */}
      <PressRelease data={companyData.pressReleases} />

      {/* Patents Component */}
      <Patents data={companyData.patents} />
    </div>
  );
};

export default Result;
