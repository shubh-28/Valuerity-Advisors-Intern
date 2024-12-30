import './Result.css';
import React, { useState } from 'react';


const GoogleNews = ({ data }) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const itemsPerPage = 3;
  
  // Show only the first 15 news items
  const limitedData = Array.isArray(data) ? data.slice(0, 15) : [];
  
  if (limitedData.length === 0) {
    return <div>No news available for the selected company.</div>;
  }

  const totalPages = Math.ceil(limitedData.length / itemsPerPage);
  
  const nextSlide = () => {
    setCurrentIndex((prev) => 
      prev + itemsPerPage >= limitedData.length ? 0 : prev + itemsPerPage
    );
  };
  
  const prevSlide = () => {
    setCurrentIndex((prev) => 
      prev - itemsPerPage < 0 ? 
        Math.max(0, limitedData.length - itemsPerPage) : 
        prev - itemsPerPage
    );
  };

  const goToPage = (pageIndex) => {
    setCurrentIndex(pageIndex * itemsPerPage);
  };

  const visibleItems = limitedData.slice(
    currentIndex,
    currentIndex + itemsPerPage
  );

  return (
    <div className="google-news">
      <h2>Google News</h2>
      
      <div className="carousel-container">
        {/* Navigation Buttons */}
        <button
          onClick={prevSlide}
          className="nav-button prev-button"
          aria-label="Previous slide"
        >
          ←
        </button>
        
        {/* News Cards Container */}
        <div className="news-container">
          {visibleItems.map((newsItem, index) => (
            <div
              key={currentIndex + index}
              className="news-tile"
            >
              <a
                href={newsItem.link}
                target="_blank"
                rel="noopener noreferrer"
                className="news-link"
              >
                <h3>{newsItem.title}</h3>
                <p className="news-time">{newsItem.time}</p>
              </a>
            </div>
          ))}
        </div>

        <button
          onClick={nextSlide}
          className="nav-button next-button"
          aria-label="Next slide"
        >
          →
        </button>
      </div>

      {/* Pagination Dots */}
      <div className="pagination">
        {Array.from({ length: totalPages }).map((_, idx) => (
          <button
            key={idx}
            onClick={() => goToPage(idx)}
            className={`pagination-dot ${
              Math.floor(currentIndex / itemsPerPage) === idx ? 'active' : ''
            }`}
            aria-label={`Go to page ${idx + 1}`}
          />
        ))}
      </div>
    </div>
  );
};

export default GoogleNews;