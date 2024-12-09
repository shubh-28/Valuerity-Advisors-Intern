

import React from "react";
import "./Result.css";

const CapterraRating = ({ data }) => {
  if (!data || data.length === 0) {
    return (
      <div className="rating-component capterra">
        <h2 className="rating-title">Capterra Rating</h2>
        <p>No ratings available for this company.</p>
      </div>
    );
  }

  return (
    <div className="rating-component capterra">
      <h2 className="rating-title">Capterra Rating</h2>
      <ul className="ratings-list">
        {data.map((item, index) => (
          <li key={index} className="rating-item">
            <span className="software-name">{item.name}</span>:{" "}
            <span className="software-rating">{item.rating}</span>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CapterraRating;
