import React from 'react';
import './Result.css';

const EmployeeReviews = () => {
  const reviews = [
    { title: 'Amazing Experience', text: 'Great company to work for!', rating: 5 },
    { title: 'Work-Life Balance', text: 'Decent, but could improve work-life balance.', rating: 4 },
    { title: 'Supportive Management', text: 'The management is supportive.', rating: 4.5 },
    { title: 'Long Hours', text: 'Nice office environment but long hours.', rating: 3.5 },
  ];

  return (
    <div className="employee-reviews">
      <h2>Employee Reviews</h2>
      <div className="reviews-grid">
        {reviews.map((review, index) => (
          <div key={index} className="review">
            <h3 className="review-title">{review.title}</h3>
            <p className="review-text">{review.text}</p>
            <p className="review-rating">Rating: {review.rating}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default EmployeeReviews;
