// import React from 'react';
// import './Result.css';

// const Patents = () => {
//   const patents = [
//     'Patent 1: Innovative AI algorithm for predictive analytics.',
//     'Patent 2: New materials for sustainable manufacturing.',
//     'Patent 3: Advanced robotics technology.',
//     'Patent 4: Next-gen data encryption method.',
//     'Patent 5: Proprietary software for real-time analytics.',
//   ];

//   return (
//     <div className="patents">
//       <h2>Patents</h2>
//       <ul>
//         {patents.map((patent, index) => (
//           <li key={index}>{patent}</li>
//         ))}
//       </ul>
//     </div>
//   );
// };

// export default Patents;


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
