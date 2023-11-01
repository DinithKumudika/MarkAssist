// TableComponent.js
import React from 'react';

const TeacherMarksTable = ({ data, columns }) => {
  const renderHeader = () => {
    return (
      <thead>
        <tr>
          {columns.map((column) => (
            <th key={column.id}>{column.header}</th>
          ))}
        </tr>
      </thead>
    );
  };

  const renderBody = () => {
    return (
      <tbody>
        {data.map((row, index) => (
          <tr key={index}>
            {columns.map((column) => (
              <td key={column.id + index}>{row[column.id]}</td>
            ))}
          </tr>
        ))}
      </tbody>
    );
  };

  return (
    <table  style={{ border: '1px solid black' }}>
      {renderHeader()}
      {renderBody()}
    </table>
  );
};

export default TeacherMarksTable;
