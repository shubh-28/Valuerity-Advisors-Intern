import React from 'react';
import './Result.css';

const PressRelease = () => {
  const pressReleases = [
    'Company launches new product line.',
    'Quarterly earnings report published.',
    'New CEO appointed to drive growth.',
    'Company announces new partnership with XYZ.',
    'Awarded for excellence in customer service.',
  ];

  return (
    <div className="press-release-container">
      <h2 className="section-heading">Press Release</h2>
      <div className="press-release">
        <ol>
          {pressReleases.map((release, index) => (
            <li key={index}>{release}</li>
          ))}
        </ol>
      </div>
    </div>
  );
};

export default PressRelease;
