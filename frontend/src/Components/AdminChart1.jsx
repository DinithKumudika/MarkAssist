import React from 'react';
import Chart from 'react-apexcharts';

function AdminChart1() {
  const value = [70]; // Represents 70 percent
  const options = {
    // chart: {
    //   width: 100, // Adjust the width of the chart
    //   height: 100, // Adjust the height of the chart
    //   type: 'radialBar',
    // },
    labels: ["Papers Graded "], // Label of the diagram
    colors: ['#304ffe'],
  };

  return (
    <div className='relative w-auto pb-4 ml-2 overflow-x-auto bg-gray-300 shadow-md sm:rounded-lg lg:mb-4 lg:w-4/6 lg:ml-10'>
      <div id="chart">
        <Chart type="radialBar" series={value} options={options} className="lg:w-auto align-self: flex-start;"/>
      </div>
      <div className='mb-1 text-base font-semibold text-center text-black-950'><span className='text-lg font-bold text-green-600'>"700"</span> Papers are Graded</div>
      <div className='text-base font-semibold text-center text-black-950'><span className='text-lg font-bold text-red-600'>"300"</span> Papers are Not Graded</div>
    </div>
  );
}

export default AdminChart1;


