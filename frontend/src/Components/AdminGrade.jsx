import React, { useState } from "react";
import { HiMenuAlt3 } from "react-icons/hi";
import { MdOutlineDashboard } from "react-icons/md";
import { RiSettings4Line } from "react-icons/ri";
import { TbReportAnalytics } from "react-icons/tb";
// import { AiOutlineUser, AiOutlineHeart } from "react-icons/ai";
import { FiFolder, FiShoppingCart } from "react-icons/fi";
import { Link } from "react-router-dom";
import classnames from "classnames";
// import BreadCrumb from "../BreadCrumb";

const AdminGrade = ({clicked, data}) => {
  const classes = classnames('sidebar static max-sm:ml-16 pt-[52px]');
  return (
    <div className={`${classes} ${clicked === 'outer' ? ' ml-16 outer w-[calc(100vw-64px)]' : 'ml-64 w-[calc(100vw-256px)] inner'} max-sm:16 max-sm:w-[calc(100vw-64px)]`}>
     <div className="flex bg-gray-300 lg:cols-1"> {/*gap-6 */}
     <div className="w-full bg-white">

<div class="grid grid-cols-1 sm:grid-cols-2 sm:gap-1 lg:grid-cols-2 xl:grid-cols-1 w-full pt-3 text-white " style={{backgroundSize: "cover"}}>

  {/* first compo */}
<div class="p-6 md:p-10 rounded-md lg:h-auto sm:h-auto grid grid-cols-1 ml-2 shadow-inner">
<div className="text-lg font-semibold text-center text-slate-950">Publish all grades</div>
<div className="font-medium text-center text-md text-slate-950">All grades will be published to the students including Grades, Marks, GPA</div>
<div className="flex justify-center object-center mt-5">
<button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded w-3/4 ">
Proceed
</button>
</div>
</div>
</div>

<div className="text-lg font-semibold text-center text-slate-950">Configure marks</div>
  <div className="font-medium text-center text-md text-slate-950">Configure your marks, Grade, GPA</div>
<div className="grid grid-cols-1 mr-2">

<div className="flex justify-center w-5/6 ">
{/* <div>
<h1>Sample Table</h1>
<TeacherMarksTable data={data} columns={columns} />
</div> */}
<table class="shadow-lg bg-white border-separate border-spacing-x-14 border-spacing-y-2 rounded text-center mt-5 w-5/6 justify-center">
<tr className="h-8">
<th class=" px-8 py-4 rounded text-center ">Mark Range</th>
<th class="text-center px-8 py-4 rounded">Grade</th>
<th class="text-center px-8 py-4 rounded">GPA</th>
</tr>
<tr className="h-8">
<td class="border px-8 py-4 rounded bg-gray-200">85-100</td>
<td class="border px-8 py-4 rounded bg-gray-200">A+</td>
<td class="border px-8 py-4 rounded bg-gray-200">4.00</td>
</tr>
<tr className="h-8">
<td class="border px-8 py-4 rounded bg-gray-200">70-84</td>
<td class="border px-8 py-4 rounded bg-gray-200">A</td>
<td class="border px-8 py-4 rounded bg-gray-200">4.00</td>
</tr>
<tr className="h-8">
<td class="border px-8 py-4 rounded bg-gray-200">65-69</td>
<td class="border px-8 py-4 rounded bg-gray-200">A-</td>
<td class="border px-8 py-4 rounded bg-gray-200">3.70</td>
</tr>
<tr className="h-8">
<td class="border px-8 py-4 rounded bg-gray-200">60-64</td>
<td class="border px-8 py-4 rounded bg-gray-200">B+</td>
<td class="border px-8 py-4 rounded bg-gray-200">3.30</td>
</tr>
<tr className="h-8">
<td class="border px-8 py-4 rounded bg-gray-200">55-59</td>
<td class="border px-8 py-4 rounded bg-gray-200">B</td>
<td class="border px-8 py-4 rounded bg-gray-200">3.00</td>
</tr>
<tr className="h-8">
<td class="border px-8 py-4 rounded bg-gray-200">50-54</td>
<td class="border px-8 py-4 rounded bg-gray-200">B-</td>
<td class="border px-8 py-4 rounded bg-gray-200">2.70</td>
</tr>
<tr className="h-8">
<td class="border px-8 py-4 rounded bg-gray-200">45-49</td>
<td class="border px-8 py-4 rounded bg-gray-200">C+</td>
<td class="border px-8 py-4 rounded bg-gray-200">2.30</td>
</tr>
<tr className="h-8">
<td class="border px-8 py-4 rounded bg-gray-200">40-44</td>
<td class="border px-8 py-4 rounded bg-gray-200">C</td>
<td class="border px-8 py-4 rounded bg-gray-200">2.00</td>
</tr>
<tr className="h-8">
<td class="border px-8 py-4 rounded bg-gray-200">35-39</td>
<td class="border px-8 py-4 rounded bg-gray-200">C-</td>
<td class="border px-8 py-4 rounded bg-gray-200">1.70</td>
</tr>
<tr className="h-8">
<td class="border px-8 py-4 rounded bg-gray-200">30-34</td>
<td class="border px-8 py-4 rounded bg-gray-200">D+</td>
<td class="border px-8 py-4 rounded bg-gray-200">1.30</td>
</tr>
<tr className="h-8">
<td class="border px-8 py-4 rounded bg-gray-200">25-29</td>
<td class="border px-8 py-4 rounded bg-gray-200">D</td>
<td class="border px-8 py-4 rounded bg-gray-200">1.00</td>
</tr>
<tr className="h-8">
<td class="border px-8 py-4 rounded bg-gray-200">00-24</td>
<td class="border px-8 py-4 rounded bg-gray-200">E</td>
<td class="border px-8 py-4 rounded bg-gray-200">F</td>
</tr>
</table>
</div>
{/* <div
className="w-auto " >
<DashboardTable2 />
</div> */}
</div>
</div>
</div>
{/* state background */}
{/* <div className="m-3 text-lg font-semibold text-gray-900">

</div> */}


</div>
  );
};

export default AdminGrade;