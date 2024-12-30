// import React, { useState, useEffect } from "react";
// import { useSearchParams, useNavigate } from "react-router-dom";
// import axios from "axios";
// import jsPDF from "jspdf"; // Import jsPDF for PDF generation
// import "./Result.css";

// // Import child components
// import GlassdoorRating from "./GlassdoorRating";
// import CapterraRating from "./CapterraRating";
// import EmployeeReviews from "./EmployeeReviews";
// import GoogleNews from "./GoogleNews";
// import PressRelease from "./PressRelease";
// import Patents from "./Patents";
// import ClinicalTrialsTable from "./ClinicalTrials";

// const Result = () => {
//   const [companyData, setCompanyData] = useState(null);
//   const [loading, setLoading] = useState(true);
//   const [error, setError] = useState(null);

//   const [searchParams] = useSearchParams();
//   const companyName = searchParams.get("query");
//   const navigate = useNavigate();

//   useEffect(() => {
//     if (!companyData && companyName) {
//       const fetchData = async () => {
//         try {
//           const response = await axios.get(
//             `http://127.0.0.1:8000/search?company_name=${encodeURIComponent(companyName)}`
//           );
//           setCompanyData(response.data);
//         } catch (err) {
//           setError("Failed to fetch data. Please try again later.");
//         } finally {
//           setLoading(false);
//         }
//       };
//       fetchData();
//     } else {
//       setError("No company name provided.");
//       setLoading(false);
//     }
//   }, [companyName]);

//   const handleDownloadJSON = () => {
//     const jsonString = JSON.stringify(companyData, null, 2);
//     const blob = new Blob([jsonString], { type: "application/json" });
//     const url = URL.createObjectURL(blob);
//     const a = document.createElement("a");
//     a.href = url;
//     a.download = `${companyData.company_name}_data.json`;
//     a.click();
//     URL.revokeObjectURL(url);
//   };

//   const handleDownloadTXT = () => {
//     let txtContent = `Company Name: ${companyData.company_name}\n\n`;
    
//     // Append other data as needed
//     if (companyData.news) {
//       txtContent += "News:\n" + companyData.news.map(item => `${item.title} - ${item.time}`).join("\n") + "\n\n";
//     }
    
//     // Add more sections as needed...
    
//     const blob = new Blob([txtContent], { type: "text/plain" });
//     const url = URL.createObjectURL(blob);
//     const a = document.createElement("a");
//     a.href = url;
//     a.download = `${companyData.company_name}_data.txt`;
//     a.click();
//     URL.revokeObjectURL(url);
//   };

//   const handleDownloadPDF = () => {
//     const doc = new jsPDF();
    
//     doc.setFontSize(20);
//     doc.text(`Company Name: ${companyData.company_name}`, 10, 10);
    
//     // Add news section
//     doc.setFontSize(16);
//     doc.text("News:", 10, 20);
    
//     if (companyData.news) {
//       companyData.news.forEach((item, index) => {
//         doc.text(`${index + 1}. ${item.title} - ${item.time}`, 10, 30 + index * 10);
//       });
//     }

//     // Add more sections as needed...

//     doc.save(`${companyData.company_name}_data.pdf`);
//   };

//   if (loading) {
//     return <div className="loading-message">Loading company insights...</div>;
//   }

//   if (error) {
//     return (
//       <div className="error-message">
//         <p>{error}</p>
//         <button className="back-button" onClick={() => navigate("/")}>Go Back to Home</button>
//       </div>
//     );
//   }

//   return (
//     <div className="result-page">
//       <button className="back-button" onClick={() => navigate("/")}>Go Back to Home</button>

//       <div className="result-header">
//         <h1 className="company-title">{companyData.company_name || "Company Insights"}</h1>
//         <p className="company-subtext">We provide comprehensive company details and metrics from various public sources.</p>
        
//         {/* Download buttons */}
//         <div className="download-buttons">
//           <button onClick={handleDownloadJSON}>Download JSON</button>
//           <button onClick={handleDownloadTXT}>Download TXT</button>
//           <button onClick={handleDownloadPDF}>Download PDF</button>
//         </div>
//       </div>

//       <div className="horizontal-components">
//         <GlassdoorRating data={companyData.glassdoor} />
//         <CapterraRating data={companyData.capterra} />
//       </div>

//       <EmployeeReviews data={companyData.reviews} />
//       <GoogleNews data={companyData.news} />
//       <PressRelease data={companyData.pressReleases} />
//       <Patents data={companyData.patents} />

//       {companyData.clinicalTrials && companyData.clinicalTrials.studies ? (
//           <ClinicalTrialsTable trials={companyData.clinicalTrials.studies} />
//       ) : (
//           <div>No clinical trials data available.</div>
//       )}
      
//     </div>
//   );
// };

// export default Result;


import React, { useState, useEffect } from "react";
import { useSearchParams, useNavigate } from "react-router-dom";
import axios from "axios";
import jsPDF from "jspdf"; // Import jsPDF for PDF generation
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

  const handleDownloadJSON = () => {
    const jsonString = JSON.stringify(companyData, null, 2);
    const blob = new Blob([jsonString], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `${companyData.company_name}_data.json`;
    a.click();
    URL.revokeObjectURL(url);
  };

  const handleDownloadTXT = () => {
    let txtContent = `Company Name: ${companyData.company_name}\n\n`;
    
    // Append structured news data
    if (companyData.news) {
      txtContent += "News:\n";
      companyData.news.forEach((item, index) => {
        txtContent += `${index + 1}. ${item.title} - ${item.time}\n`; // Numbering each news item
      });
      txtContent += "\n"; // Add a newline after news section
    }

    // Append structured reviews data
    if (companyData.reviews) {
      txtContent += "Employee Reviews:\n";
      companyData.reviews.forEach((review, index) => {
        txtContent += `${index + 1}. ${review.comment}\n`; // Numbering each review
      });
      txtContent += "\n"; // Add a newline after reviews section
    }

    // Add more sections as needed...

    const blob = new Blob([txtContent], { type: "text/plain" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `${companyData.company_name}_data.txt`;
    a.click();
    URL.revokeObjectURL(url);
  };

  const handleDownloadPDF = () => {
    const doc = new jsPDF();
    
    doc.setFontSize(20);
    doc.text(`Company Name: ${companyData.company_name}`, 10, 10);
    
    // Add news section
    doc.setFontSize(16);
    doc.text("News:", 10, 20);
    
    if (companyData.news) {
      companyData.news.forEach((item, index) => {
        doc.text(`${index + 1}. ${item.title} - ${item.time}`, 10, 30 + index * 10); // Numbering each news item
      });
      doc.text("", 10, 40 + companyData.news.length * 10); // Add spacing after news section
    }

    // Add employee reviews section
    if (companyData.reviews) {
      doc.setFontSize(16);
      doc.text("Employee Reviews:", 10, doc.internal.getNumberOfPages() * 10 + 10); // Positioning based on current page height
      companyData.reviews.forEach((review, index) => {
        doc.text(`${index + 1}. ${review.comment}`, 10, doc.internal.getNumberOfPages() * 10 + (index + 1) * 10); // Numbering each review
      });
    }

    // Add more sections as needed...

    doc.save(`${companyData.company_name}_data.pdf`);
  };

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
        
        {/* Download buttons */}
        <div className="download-buttons">
          <button onClick={handleDownloadJSON}>Download JSON</button>
          <button onClick={handleDownloadTXT}>Download TXT</button>
          <button onClick={handleDownloadPDF}>Download PDF</button>
        </div>
      </div>

      <div className="horizontal-components">
        <GlassdoorRating data={companyData.glassdoor} />
        <CapterraRating data={companyData.capterra} />
      </div>

      <EmployeeReviews data={companyData.reviews} />
      <GoogleNews data={companyData.news} />
      <PressRelease data={companyData.pressReleases} />
      <Patents data={companyData.patents} />

      {companyData.clinicalTrials && companyData.clinicalTrials.studies ? (
          <ClinicalTrialsTable trials={companyData.clinicalTrials.studies} />
      ) : (
          <div>No clinical trials data available.</div>
      )}
      
    </div>
  );
};

export default Result;
