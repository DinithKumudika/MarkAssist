import React from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

function TeacherChart() {
  const data = [
    {
      name: 'A+',
      uv: 40,
      student: 24,
      amt: 2400,
    },
    {
      name: 'A',
      uv: 3000,
      student: 13,
      amt: 2210,
    },
    {
      name: 'A-',
      uv: 2000,
      student: 98,
      amt: 2290,
    },
    {
      name: 'B+',
      uv: 2780,
      student: 39,
      amt: 2000,
    },
    {
      name: 'B',
      uv: 1890,
      student: 75,
      amt: 2181,
    },
    {
      name: 'B-',
      uv: 2390,
      student: 85,
      amt: 2500,
    },
    {
      name: 'C+',
      uv: 3490,
      student: 10,
      amt: 2100,
    },
    {
      name: 'C',
      uv: 4000,
      student: 50,
      amt: 2400,
    },
    {
      name: 'C-',
      uv: 4000,
      student: 5,
      amt: 2400,
    },
    {
      name: 'D+',
      uv: 4000,
      student: 2,
      amt: 2400,
    },
    {
      name: 'D',
      uv: 4000,
      student: 4,
      amt: 2400,
    },
    {
      name: 'E',
      uv: 4000,
      student: 10,
      amt: 2400,
    },
    {
      name: 'F',
      uv: 4000,
      student: 3,
      amt: 2400,
    },
  ];

  return (
    <ResponsiveContainer width="100%" height={320}>
      <BarChart
        width={500}
        height={200}
        data={data}
        margin={{
          top: 5,
          right: 30,
          left: 20,
          bottom: 5,
        }}
        barSize={20}
      >
        <XAxis dataKey="name" scale="point" padding={{ left: 10, right: 10 }} />
        <YAxis />
        <Tooltip />
        <Legend />
        <CartesianGrid strokeDasharray="" />
        <Bar dataKey="student" fill="#361fbd" background={{ fill: '#dddce4' }} />
      </BarChart>
    </ResponsiveContainer>
  );
}

export default TeacherChart;
