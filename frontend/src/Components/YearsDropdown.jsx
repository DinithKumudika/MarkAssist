import React from 'react';
import Select from 'react-select';

const aquaticCreatures = [
  { label: '2018', value: '2018' },
  { label: '2019', value: '2019' },
  { label: '2020', value: '2020' },
  { label: '2021', value: '2021' },
  { label: '2022', value: '2022' },
  { label: '2023', value: '2023' },
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