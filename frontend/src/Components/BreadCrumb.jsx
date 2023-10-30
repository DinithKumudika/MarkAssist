import React, { useEffect, useState } from 'react'

function BreadCrumb({props}) {
  console.log("props::",props);
    const [currentDateTime, setCurrentDateTime] = useState(new Date());

    useEffect(() => {
      const intervalId = setInterval(() => {
        setCurrentDateTime(new Date());
      }, 60000); // Update every second
  
      // Clean up the interval when the component unmounts
      return () => clearInterval(intervalId);
    }, []);
  
    // Set the desired time zone (e.g., "America/New_York")
    const timeZone = "Asia/Colombo"; // Replace with your desired time zone
  
    const dateFormatOptions = {
        timeZone,
        year: "numeric",
        month: "long",
        day: "numeric",
      };
      
      const timeFormatOptions = {
        timeZone,
        hour: "numeric",
        minute: "numeric",
        hour12: false, // Use 24-hour format
      };
  
    const formattedDate = currentDateTime.toLocaleDateString('en-US', dateFormatOptions);
    const formattedTime = currentDateTime.toLocaleTimeString('en-US', timeFormatOptions);
  

  return (
    <div class="grid-cols-1 gap-4 lg:grid-cols-3 lg:gap-8 bg-white h-auto flex justify-between rounded p-5 my-4">
        <div className="text-lg text-gray-500 font-bold">
          Student Dashboard
          <div className="text-base text-gray-400">
            Home
          </div>
        </div>
        <div className="text-base text-gray-500 flex flex-col items-end">
            <div>
                {formattedTime}
            </div>
            <div>
                {formattedDate}
            </div>
        </div>
    </div>
  )
}

export default BreadCrumb
