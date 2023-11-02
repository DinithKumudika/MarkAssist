import React from 'react'

function ConfigureCompo() {
  return (
       <div className="container mx-auto relative  top-32 w-4/5 lg:w-4/5 pr-15 pl-5 pt-1 mb-6 ">
       
       <h2 class=" mb-4 text-lg font-bold leading-none tracking-tight text-gray-900 md:text-2xl lg:text-2xl dark:text-black w-1/4 object-center lg:ml-96 ml-48 text-center">Configure marks</h2>
       <p class=" text-base font-normal text-gray-500 lg:text-lg sm:px-16 xl:px-48 dark:text-gray-400 mb-16 ml-16 mr-4 w-4/5 lg:w-max sm:text-center lg:text-left">Add marks allocated for each range(mark for students answer obtained accuracy)</p>

      <div className="grid items-center justify-center w-3/4 h-32 grid-flow-row-dense grid-cols-4 grid-rows-2 mt-5 gap-x-8 ml-28 lg:ml-48">
    <div class="flex flex-col gap-x-8 gap-y-4 text-center">
      Minimum
      <div className="w-4/5 h-10 pt-2 rounded bg-gray-200">0</div>
      <div className="w-4/5 h-10 pt-2 rounded bg-gray-200">70%</div>
      </div>
      <div className="flex flex-col text-center gap-x-8 gap-y-4">Maximum
      <div className="w-4/5 h-10 pt-2 rounded bg-gray-200">30%</div>
      <div className="w-4/5 h-10 pt-2 rounded bg-gray-200">100%</div>
      </div>
      <div className="flex flex-col text-center gap-x-8 gap-y-4">Marks
      <div className="w-4/5 h-10 pt-2 rounded bg-gray-200">5</div>
      <div className="w-4/5 h-10 pt-2 rounded bg-gray-200">10</div>
      </div>
      
      <div className="flex flex-col mt-10 text-center gap-x-8 gap-y-4">
      <button className="w-1/5 h-10 pt-2 rounded bg-gray-200 text-xl md:ml-14"> -
      
       </button>
       
      <button className="w-1/5 h-10 pt-2 rounded bg-gray-200 text-xl md:ml-14"> +
      
        </button>
      </div>
      
      </div>
      <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 border border-blue-700 rounded w-2/3 mb-8 ml-28 lg:ml-48">
  Proceed
</button>
      </div>
      
  
  )
}

export default ConfigureCompo



