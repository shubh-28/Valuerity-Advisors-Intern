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
    <div className="press-release">
      <h2>Press Release</h2>
      <ul>
        {pressReleases.map((release, index) => (
          <li key={index}>{release}</li>
        ))}
      </ul>
    </div>
  );
};

export default PressRelease;
