import React from 'react'

function Table1Row() {
  return (
    <div className="">
      <div className="grid content-center w-full h-4 grid-cols-5 p-5 mt-6 ml-0 text-gray-700 bg-white bg-center rounded-none gap-x-9 gap-y-1">
      <div>Rushin Sandeepana</div>
      <div>Assistant lecturer</div>
      <div>2020.06.30</div>
      <div>03</div>
      <div><svg class="h-6 w-6 text-black mt-1"  viewBox="0 0 24 24"  fill="none"  stroke="currentColor"  stroke-width="2"  stroke-linecap="round"  stroke-linejoin="round">  <circle cx="12" cy="12" r="1" />  <circle cx="12" cy="5" r="1" />  <circle cx="12" cy="19" r="1" /></svg></div>
      {/* <p className="text-lg text-gray-500">
        React and Tailwind CSS in action
      </p> */}
    </div>
    </div>
  )
}

export default Table1Row
