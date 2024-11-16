import React from 'react';
import './Result.css';

const CapterraRating = () => {
  const ratings = [4.0, 4.2, 3.8, 4.5, 4.1];

  return (
    <div className="rating-component capterra">
      <h2 className="rating-title">Capterra Rating</h2>
      <ul className="ratings-list">
        {ratings.map((rating, index) => (
          <li key={index} className="rating-item">
            {rating}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CapterraRating;
