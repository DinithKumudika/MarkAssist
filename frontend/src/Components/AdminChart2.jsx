import React from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

function TeacherChart() {
  const data = [
    {
      name: 'Year1',
      uv: 40,
      Papers: 24,
      amt: 2400,
    },
    {
      name: 'Year2',
      uv: 3000,
      Papers: 13,
      amt: 2210,
    },
    {
      name: 'Year3',
      uv: 2000,
      Papers: 98,
      amt: 2290,
    },
    {
      name: 'Year4',
      uv: 2780,
      Papers: 39,
      amt: 2000,
    },
  ];

  return (
    <ResponsiveContainer width="100%" height={320} className="lg:mb-2 lg:w-5/6 ">
      <BarChart
        width={700}
        height={200}
        data={data}
        margin={{
          top: 5,
          right: 30,
          left: 20,
          bottom: 5,
        }}
        barSize={45}
      >
        <XAxis dataKey="name" scale="point" padding={{ left: 20, right: 20 }} />
        <YAxis />
        <Tooltip />
        <Legend />
        <CartesianGrid strokeDasharray="" />
        <Bar dataKey="Papers" fill="#361fbd" background={{ fill: '#dddce4' }} />
      </BarChart>
    </ResponsiveContainer>
  );
}

export default TeacherChart;
