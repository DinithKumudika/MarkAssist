import DragDrop from '../DragDrop'
import Table from '../Table'
import classnames from 'classnames'
import { AiOutlinePlus } from "react-icons/ai";
import { BiFilter } from "react-icons/bi";
import { useState } from 'react'
function AnswerSheets({clicked, data}) {
  const classes = classnames('sidebar static max-sm:ml-16 pt-[80px]');
  const [show, setShow] = useState(false);
  // console.log("DATA:"+data.id)
  const handleCKick = () => {
    setShow((prev)=>!prev);
    // console.log(show);
  }

  const closeModal = () =>{
    setShow(false);
  }

  return (
    <div className={`${classes} ${clicked === 'outer' ? ' ml-16 outer w-[calc(100vw-64px)]' : 'ml-64 w-[calc(100vw-256px)] inner'} max-sm:16 max-sm:w-[calc(100vw-64px)]`}>
      {data ? (
        <div className=' flex flex-col items-center justify-top w-full h-full px-10 max-sm:px-4 py-8'>
            <div className='mb-12 text-center  w-full'>
              <p className='text-xl font-bold text-[#191854]'>Answer Sheets</p>
              <p className='text-lg text-black opacity-60'>Upload answer papers</p>
            </div>
            <div className='px-12 max-sm:px-4 flex flex-row justify-between w-full'>
              <button className="rounded rounded-sm bg-custom-blue-2 w-40 max-sm:w-20 h-9 mr-2 text-white flex justify-center items-center flex-row" onClick={handleCKick}><AiOutlinePlus/><div className='ml-2'>Upload</div></button>
              <button className="rounded rounded-sm bg-custom-blue-2 w-40 max-sm:w-20 h-9 mr-2 text-white flex justify-center items-center flex-row"><BiFilter/><div className='ml-2'>Filter</div></button>
              <form className='w-3/4 ' >
                <input className="rounded shadow shadow-gray-600 w-full h-9 p-2 mb-4" type="text" placeholder='Search'/>
              </form>
            </div>
            <Table name={true} date={true} select={true} AnswerSheets={data}/>
        </div>
      ): ( 
        <DragDrop closeFunc={closeModal}>Answer Sheets</DragDrop>
      )}
      {show && <DragDrop closeFunc={closeModal}>Answer Sheets</DragDrop>}
    </div>
  )
}

export default AnswerSheets
