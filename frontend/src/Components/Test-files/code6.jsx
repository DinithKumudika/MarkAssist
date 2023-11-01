import DragDrop from '../DragDrop'
import classnames from 'classnames'
import { AiOutlinePlus } from "react-icons/ai";
import { BiFilter } from "react-icons/bi";
import { useState } from 'react'
function AnswerSheets({clicked, data}) {
  const classes = classnames('sidebar static max-sm:ml-16');
  const [show, setShow] = useState(false);

  const handleCKick = () => {
    setShow((prev)=>!prev);
    // console.log(show);
  }

  const closeModal = () =>{
    setShow(false);
  }

  return (
    <div className={`${classes} ${clicked === 'outer' ? 'ml-16 outer' : 'ml-64 inner'}`}>
      {data ? (
        <div className=' flex flex-col items-center justify-center w-full h-full px-10 max-sm:px-4 py-8'>
            <div className='mb-12 text-center  w-full'>
              <p className='text-xl font-bold text-[#191854]'>Answer Sheets</p>
              <p className='text-lg text-black opacity-60'>Upload a new one or change the previous one</p>
            </div>
            <div className='px-12 max-sm:px-4 flex flex-row justify-between w-full'>
              <button className="rounded rounded-sm bg-[#4457FF] w-40 max-sm:w-20 h-9 mr-2 text-white flex justify-center items-center flex-row" onClick={handleCKick}><AiOutlinePlus/><div className='ml-2'>Upload</div></button>
              <button className="rounded rounded-sm bg-[#4457FF] w-40 max-sm:w-20 h-9 mr-2 text-white flex justify-center items-center flex-row"><BiFilter/><div className='ml-2'>Filter</div></button>
              <form className='w-3/4 ' >
                <input className="rounded shadow shadow-gray-600 w-full h-9 p-2 mb-4" type="text" placeholder='Search'/>
              </form>
            </div>
            <div className='w-full px-12 max-sm:px-4 overflow-auto'>
              <table className='w-full'>
                <thead className='bg-[#D9D9D9] sticky'>
                <tr>
                  <th className='text-xl h-8 font-bold opacity-60 w-3/12'>Select</th>
                  <th className='text-xl h-8 font-bold opacity-60 w-3/12'>Select</th>
                  <th className='text-xl h-8 font-bold opacity-60 w-3/12'>Select</th>                  
                </tr>
                </thead>
                <tbody>
                {/* {data.map((item) => (
                      <tr key={item.id}>
                        <td>{item.id}</td>
                        <td>{item.name}</td>
                        <td>{item.age}</td>
                      </tr>
                    ))} */}
                    <tr>
                      <td className='text-lg px-4 max-sm:px-1 h-10 border-y-2 border-x-2 font-medium opacity-60'>SCS2213-DSA-2023</td>
                      <td className='text-lg px-4 max-sm:px-1 h-10 border-y-2 border-x-4 font-medium opacity-60'>10/06/2023</td>
                      <td className='flex justify-center text-sm px-4 h-10 border-y-2 border-x-2 font-medium'><button className="rounded rounded-xl bg-[#4457FF] w-32 max-sm:w-20 h-8 mr-2 text-white flex justify-center items-center flex-row"><div className='ml-2'>Select</div></button></td>
                    </tr>
                    {/* <tr>
                      <td className='text-lg px-4 max-sm:px-1 h-10 border-y-2 border-x-2 font-medium opacity-60'>Hello</td>
                      <td className='text-lg px-4 max-sm:px-1 h-10 border-y-2 border-x-4 font-medium opacity-60'>Hello</td>
                      <td className='flex justify-center text-sm px-4 h-10 border-y-2 border-x-2 font-medium'><button className="rounded rounded-xl bg-[#4457FF] w-32 max-sm:w-20 h-8 mr-2 text-white flex justify-center items-center flex-row"><div className='ml-2'>Select</div></button></td>
                    </tr>
                    <tr>
                      <td className='text-lg px-4 max-sm:px-1 h-10 border-y-2 border-x-2 font-medium opacity-60'>Hello</td>
                      <td className='text-lg px-4 max-sm:px-1 h-10 border-y-2 border-x-4 font-medium opacity-60'>Hello</td>
                      <td className='flex justify-center text-sm px-4 h-10 border-y-2 border-x-2 font-medium'><button className="rounded rounded-xl bg-[#4457FF] w-32 max-sm:w-20 h-8 mr-2 text-white flex justify-center items-center flex-row"><div className='ml-2'>Select</div></button></td>
                    </tr> */}
                </tbody>
              </table>
            </div>
        </div>
      ): ( 
        "<DragDrop/>"
      )}
      {show && <DragDrop closeFunc={closeModal}>Answer Sheets</DragDrop>}
    </div>
  )
}

export default AnswerSheets
