import React from 'react'

function DashboardTable2() {
  return (
    <div>
      
 <div class="relative overflow-x-auto shadow-md sm:rounded-lg w-auto lg:mb-4 ml-2"> {/*xl:mt-10*/}
    <div class="flex items-center justify-between py-3 bg-white dark:bg-gray-300">
        <div className="ml-5 text-xl font-semibold text-gray-500">First Year - Semester 1</div>
    </div>
    <table class="w-full text-sm text-left text-gray-300 dark:text-gray-200 table-auto">
        <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-300 dark:text-gray-400">
            <tr>
                {/* <th scope="col" class="p-4">
                    <div class="flex items-center">
                        <input id="checkbox-all-search" type="checkbox" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600" />
                        <label for="checkbox-all-search" class="sr-only">checkbox</label>
                    </div>
                </th> */}
                <th scope="col" class="px-9 py-0 ">
                    Subject
                </th>
                <th scope="col" class="px-16 py-0">
                    Grade
                </th>
                {/* <th scope="col" class="px-6 py-3">
                    Status
                </th>
                <th scope="col" class="px-6 py-3">
                    Action
                </th> */}
            </tr>
        </thead>
        <tbody>
            <tr class="bg-white border-b dark:bg-gray-300 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600 ">
                {/* <td class="w-4 p-4">
                   
               </td> */}
                <th scope="row" class="flex items-center px-6 py-2 text-gray-900 whitespace-nowrap dark:text-white">
                    
                    <div class="pl-3">
                        <div class="text-base font-semibold text-violet-950">Interactive Media Design</div>
                        <div class="font-normal text-gray-800">Subject Code : IS 1107 / Credit: 3
                        
                        </div>
                    </div>  
                </th>
                <td class="px-16 py-4 text-violet-950 font-semibold">
                A+
                </td>
                
                
            </tr>
            <tr class="bg-white border-b dark:bg-gray-300 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                {/* <td class="w-4 p-4">
                    <div class="flex items-center">
                        <input id="checkbox-table-search-2" type="checkbox" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600" />
                    </div>
                </td> */}
                <th scope="row" class="flex items-center px-6 py-2 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                    <div class="pl-3">
                        <div class="text-base font-semibold text-violet-950">Interactive Media Design</div>
                        <div class="font-normal text-gray-800">Subject Code : IS 1107 / Credit: 3</div>
                    </div>
                </th>
                <td class="px-16 py-4 text-violet-950 font-semibold">
                    A+
                </td>
                
            </tr>
            <tr class="bg-white border-b dark:bg-gray-300 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                {/* <td class="w-4 p-4">
                    <div class="flex items-center">
                        <input id="checkbox-table-search-2" type="checkbox" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600" />
                        <label for="checkbox-table-search-2" class="sr-only">checkbox</label>
                    </div>
                </td> */}
                <th scope="row" class="flex items-center px-6 py-2 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                    <div class="pl-3">
                        <div class="text-base font-semibold text-violet-950">Interactive Media Design</div>
                        <div class="font-normal text-gray-800">Subject Code : IS 1107 / Credit: 3</div>
                    </div>
                </th>
                <td class="px-16 py-4 text-violet-950 font-semibold">
                    A+
                </td>
                
            </tr>
            <tr class="bg-white border-b dark:bg-gray-300 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                {/* <td class="w-4 p-4">
                    <div class="flex items-center">
                        <input id="checkbox-table-search-2" type="checkbox" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600" />
                        <label for="checkbox-table-search-2" class="sr-only">checkbox</label>
                    </div>
                </td> */}
                <th scope="row" class="flex items-center px-6 py-2 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                    <div class="pl-3">
                        <div class="text-base font-semibold text-violet-950">Interactive Media Design</div>
                        <div class="font-normal text-gray-800">Subject Code : IS 1107 / Credit: 3</div>
                    </div>
                </th>
                <td class="px-16 py-4 text-violet-950 font-semibold">
                    A+
                </td>
                
            </tr>
            <tr class="bg-white dark:bg-gray-300 hover:bg-gray-50 dark:hover:bg-gray-600">
                {/* <td class="w-4 p-4">
                    <div class="flex items-center">
                        <input id="checkbox-table-search-3" type="checkbox" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600" />
                        <label for="checkbox-table-search-3" class="sr-only">checkbox</label>
                    </div>
                </td> */}
                <th scope="row" class="flex items-center px-6 py-2 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                    
                    <div class="pl-3">
                        <div class="text-base font-semibold text-violet-950">Interactive Media Design</div>
                        <div class="font-normal text-gray-800">Subject Code : IS 1107 / Credit: 3</div>
                    </div>
                </th>
                <td class="px-16 py-4 text-violet-950 font-semibold">
                    A+
                </td>
                
            </tr>
        </tbody>
    </table>
    
   
</div>

    </div>
  )
}

export default DashboardTable2;
