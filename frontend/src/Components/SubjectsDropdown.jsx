import React from 'react';
import Select from 'react-select';

const aquaticCreatures = [
  { label: 'Data Structure and Algorithms', value: 'Data Structure and Algorithms' },
  { label: 'Database Management', value: 'Database Management' },
  { label: 'Human Computer Interaction', value: 'Human Computer Interaction' },
  { label: 'Software Project Management', value: 'Software Project Management' },
  { label: 'Software Quality Assurance', value: 'Software Quality Assurance' },
  { label: 'Professional Practice', value: 'Professional Practice' },
];
const customStyles = {
  control: (provided) => ({
    ...provided,
    background: '#e5e7eb', // Change this to the desired background color
  }),
  option: (provided) => ({
    ...provided,
    background: '#e5e7eb', // Change this to the desired background color for options
  }),
};

function App() {
  return (
    <div className=" App">
      <Select className='text-gray-800'
        options={aquaticCreatures}
        styles={customStyles} 
      />
    </div>
  );
}

export default App;