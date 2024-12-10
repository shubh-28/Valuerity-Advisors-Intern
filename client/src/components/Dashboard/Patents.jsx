import React from 'react';
import './Result.css';

const Patents = ({ data }) => {
  // Ensure there is data to display
  if (!data || data === "No patents found or unable to retrieve patents.") {
    return (
      <div className="patents">
        <h2>Patents</h2>
        <p>No patents found for this company.</p>
      </div>
    );
  }

  return (
    <div className="patents">
      <h2>Patents</h2>
      <ul>
        {data.split('\n').map((patent, index) => (
          <li key={index}>{patent}</li>
        ))}
      </ul>
    </div>
  );
};

export default Patents;
