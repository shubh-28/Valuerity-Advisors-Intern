import React from 'react';

const styles = {
  container: {
    backgroundColor: '#ffffff',
    padding: '20px',
    margin: '0px',
    borderRadius: '8px',
    boxShadow: '0 1px 3px rgba(0, 0, 0, 0.1)',
  },
  tableContainer: {
    width: '100%',
    backgroundColor: '#ffffff',
    borderRadius: '8px',
    boxShadow: '0 1px 3px rgba(0, 0, 0, 0.1)',
  },
  header: {
    padding: '16px',
    borderBottom: '1px solid #e5e7eb',
  },
  headerTitle: {
    fontSize: '25px',
    fontWeight: '600',
    margin: 0,
  },
  tableWrapper: {
    padding: '16px',
    overflowX: 'auto',
  },
  table: {
    width: '100%',
    borderCollapse: 'collapse',
    minWidth: '800px',
  },
  th: {
    padding: '12px 16px',
    textAlign: 'left',
    fontSize: '14px',
    fontWeight: '500',
    color: '#6b7280',
    backgroundColor: '#f9fafb',
    textTransform: 'uppercase',
    whiteSpace: 'nowrap',
    borderBottom: '1px solid #e5e7eb',
  },
  td: {
    padding: '12px 16px',
    fontSize: '14px',
    color: '#111827',
    borderBottom: '1px solid #e5e7eb',
  },
  tr: {
   transition:'background-color .2s'
   },
   link:{
       color:'#2563eb'
   }
};

const ClinicalTrialsTable = ({ trials }) => {
   return (
     <div style={styles.container}>
       <div style={styles.tableContainer}>
         <div style={styles.header}>
           <h2 style={styles.headerTitle}>Clinical Trials</h2>
         </div>
         <div style={styles.tableWrapper}>
           <table style={styles.table}>
             <thead>
               <tr>
                 <th style={styles.th}>NCT ID</th>
                 <th style={styles.th}>URL</th>
                 <th style={styles.th}>Study Start</th>
                 <th style={styles.th}>Primary Completion</th>
                 <th style={styles.th}>Study Completion</th>
                 <th style={styles.th}>Enrollment</th>
                 <th style={styles.th}>Study Type</th>
                 <th style={styles.th}>Phase</th>
               </tr>
             </thead>
             <tbody>
               {trials.map((trial, index) => (
                 <tr 
                   key={trial["NCT-ID"] || index} 
                   style={styles.tr}
                   onMouseEnter={(e) => e.currentTarget.style.backgroundColor='#f9fafb'}
                   onMouseLeave={(e) => e.currentTarget.style.backgroundColor='transparent'}
                 >
                   <td style={styles.td}>{trial["NCT-ID"]}</td>
                   <td style={styles.td}>
                     <a 
                       href={trial.URL} 
                       target="_blank" 
                       rel="noopener noreferrer"
                       style={styles.link}
                     >
                       {trial.URL}
                     </a>
                   </td>
                   <td style={styles.td}>{trial["Study Start"]}</td>
                   <td style={styles.td}>{trial["Primary Completion"]}</td>
                   <td style={styles.td}>{trial["Study Completion"]}</td>
                   <td style={styles.td}>{trial.Enrollment}</td>
                   <td style={styles.td}>{trial["Study Type"]}</td>
                   <td style={styles.td}>{trial.Phase}</td>
                 </tr>
               ))}
             </tbody>
           </table>
         </div>
       </div>
     </div>
   );
};

export default ClinicalTrialsTable;
