import React from 'react';
import './Result.css';

const EmployeeReviews = () => {
  const reviews = [
    { text: 'Great company to work for!', rating: 5 },
    { text: 'Decent, but could improve work-life balance.', rating: 4 },
    { text: 'The management is supportive.', rating: 4.5 },
    { text: 'Nice office environment but long hours.', rating: 3.5 },
  ];

  return (
    <div className="employee-reviews">
      <h2>Employee Reviews</h2>
      <div className="reviews-grid">
        {reviews.map((review, index) => (
          <div key={index} className="review">
            <p className="review-text">{review.text}</p>
            <p className="review-rating">Rating: {review.rating}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default EmployeeReviews;
