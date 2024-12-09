// import React from "react";
// import "./Result.css";

// const PressRelease = ({ data }) => {
//   if (!data || data.length === 0) {
//     return (
//       <div className="press-release-container">
//         <h2 className="section-heading">Press Releases</h2>
//         <p>No press release data available.</p>
//       </div>
//     );
//   }

//   return (
//     <div className="press-release-container">
//       <h2 className="section-heading">Press Releases</h2>
//       <div className="press-release">
//         <ol>
//           {data.split("\n").map((release, index) => (
//             <li key={index}>{release}</li>
//           ))}
//         </ol>
//       </div>
//     </div>
//   );
// };

// export default PressRelease;

// Updated `PressRelease.jsx`
import React from "react";
import "./Result.css";

const PressRelease = ({ data }) => {
  if (!data || data.length === 0) {
    return (
      <div className="press-release-container">
        <h2 className="section-heading">Press Releases</h2>
        <p>No press release data available.</p>
      </div>
    );
  }

  return (
    <div className="press-release-container">
      <h2 className="section-heading">Press Releases</h2>
      <div className="press-release">
        <ol>
          {data.split("\n").map((line, index) => {
            const parts = line.split(" ");
            const link = parts.pop(); // Extract the link
            const title = parts.join(" "); // Rejoin the rest as the title
            return (
              <li key={index}>
                <a href={link} target="_blank" rel="noopener noreferrer">{title}</a>
              </li>
            );
          })}
        </ol>
      </div>
    </div>
  );
};

export default PressRelease;
