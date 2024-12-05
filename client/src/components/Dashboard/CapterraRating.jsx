import React from 'react';
import './Result.css';

const CapterraRating = () => {
  const ratings = [
    { name: 'Software A', rating: 4.0 },
    { name: 'Software B', rating: 4.2 },
    { name: 'Software C', rating: 3.8 },
    { name: 'Software D', rating: 4.5 },
    { name: 'Software E', rating: 4.1 },
  ];

  return (
    <div className="rating-component capterra">
      <h2 className="rating-title">Capterra Rating</h2>
      <ul className="ratings-list">
        {ratings.map((item, index) => (
          <li key={index} className="rating-item">
            <span className="software-name">{item.name}</span>:<span className="software-rating"> {item.rating}</span>
            </li>
        ))}
      </ul>
    </div>
  );
};

export default CapterraRating;
