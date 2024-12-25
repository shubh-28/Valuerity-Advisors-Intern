import React from "react";
import Slider from "react-slick";
import './Result.css';

const GoogleNews = ({ data }) => {
  // Show only the first 10 news items
  const limitedData = Array.isArray(data) ? data.slice(0, 15) : [];

  if (limitedData.length === 0) {
    return <div>No news available for the selected company.</div>;
  }

  // Slider settings
  const settings = {
    dots: true, // Show navigation dots
    infinite: false, // Disable infinite looping
    speed: 500, // Transition speed
    slidesToShow: 3, // Number of tiles visible at once
    slidesToScroll: 1, // Number of tiles to scroll at once
  };

  return (
    <div className="google-news">
      <h2>Google News</h2>
      <Slider {...settings}>
        {limitedData.map((newsItem, index) => (
          <div key={index} className="news-tile">
            <a
              href={newsItem.link}
              target="_blank"
              rel="noopener noreferrer"
              style={{ textDecoration: 'none', color: 'inherit' }}
            >
              <h3>{newsItem.title}</h3>
              <p className="news-time">{newsItem.time}</p>
            </a>
          </div>
        ))}
      </Slider>
    </div>
  );
};

export default GoogleNews;
