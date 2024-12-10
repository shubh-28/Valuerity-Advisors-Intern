import React from "react";
import "./Result.css";

const PressRelease = ({ data }) => {
  if (!data || data.length === 0) {
    return (
      <div className="press-release-container">
        <h2 className="section-heading">Press Releases</h2>
        <p>No press release data available.</p>
      </div>
    );
  }

  return (
    <div className="press-release-container">
      <h2 className="section-heading">Latest Press Releases</h2>
      <div className="press-release">
        {data.split("\n").map((line, index) => {
          const parts = line.split(" ");
          const link = parts.pop(); // Extract the link
          const title = parts.join(" "); // Rejoin the rest as the title
          return (
            <div key={index} className="press-release-item">
              <a href={link} target="_blank" rel="noopener noreferrer">{title}</a>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default PressRelease;


