import React from 'react';
import './Result.css';

// Import child components
import GlassdoorRating from './GlassdoorRating';
import CapterraRating from './CapterraRating';
import EmployeeReviews from './EmployeeReviews';
import GoogleNews from './GoogleNews';
import PressRelease from './PressRelease';
import Patents from './Patents';

const Result = () => {
  return (
    <div className="result-page">
      {/* Title and Subtitle */}
      <div className="result-header">
        <h1 className="company-title">Company Insights</h1>
        <p className="company-subtext">
          We provide comprehensive company details and metrics from various public sources
        </p>
      </div>

      {/* Horizontal Components */}
      <div className="horizontal-components">
        <GlassdoorRating />
        <CapterraRating />
      </div>

      {/* Employee Reviews Component */}
      <EmployeeReviews />

      {/* Google News Component */}
      <GoogleNews />

      {/* Press Release Component */}
      <PressRelease />

      {/* Patents Component */}
      <Patents />
    </div>
  );
};

export default Result;
