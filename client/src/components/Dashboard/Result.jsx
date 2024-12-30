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
import ClinicalTrialsTable from "./ClinicalTrials";

const Result = () => {
  const [companyData, setCompanyData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const [searchParams] = useSearchParams();
  const companyName = searchParams.get("query");
  const navigate = useNavigate();

  useEffect(() => {
    if (!companyData && companyName) {
      const fetchData = async () => {
        try {
          const response = await axios.get(
            `http://127.0.0.1:8000/search?company_name=${encodeURIComponent(companyName)}`
          );
          setCompanyData(response.data);
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
        <button className="back-button" onClick={() => navigate("/")}>Go Back to Home</button>
      </div>
    );
  }

  return (
    <div className="result-page">
      <button className="back-button" onClick={() => navigate("/")}>Go Back to Home</button>

      <div className="result-header">
        <h1 className="company-title">{companyData.company_name || "Company Insights"}</h1>
        <p className="company-subtext">We provide comprehensive company details and metrics from various public sources.</p>
      </div>

      <div className="horizontal-components">
        <GlassdoorRating data={companyData.glassdoor} />
        <CapterraRating data={companyData.capterra} />
      </div>

      <EmployeeReviews data={companyData.reviews} />
      <GoogleNews data={companyData.news} />
      <PressRelease data={companyData.pressReleases} />
      <Patents data={companyData.patents} />

      {/* Pass correct structure to ClinicalTrialsTable */}
      {companyData.clinicalTrials && companyData.clinicalTrials.studies ? (
          <ClinicalTrialsTable trials={companyData.clinicalTrials.studies} />
      ) : (
          <div>No clinical trials data available.</div>
      )}
      
    </div>
  );
};

export default Result;
