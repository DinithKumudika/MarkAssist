import DragDrop from '../DragDrop'
import Table from '../Table'
import classnames from 'classnames'
import { AiOutlinePlus } from "react-icons/ai";
import { BiFilter } from "react-icons/bi";
import { useState } from 'react'
function MarkingSchemes({clicked, data}) {
  const classes = classnames('sidebar static max-sm:ml-16 pt-[80px]');
  const [show, setShow] = useState(false);
  // const markingSchemas =JSON.stringify(data);
  var link = ''
  if(data){
    // console.log("DATA:"+data)
    // console.log("SubjectId:"+data.subjectId)
    // link = {link:"/markingschemes/"+data.id};
    // link = {link:"/markingschemes/"+data.id+"/"+data.subjectId};
    link = {link:"/markingschemes/"+data.subjectId};

  }
  else{
    console.log("DATAs:"+data)
  }




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
              <p className='text-xl font-bold text-[#191854]'>Marking scheme</p>
              <p className='text-lg text-black opacity-80 text-center'>Upload a new one or change the previous one</p>
            </div>
            <div className='px-12 max-sm:px-4 flex flex-row justify-between w-full'>
              <button className="rounded rounded-sm bg-[#00ADEF] w-40 max-sm:w-20 h-9 mr-2 text-white flex justify-center items-center flex-row" onClick={handleCKick}><AiOutlinePlus/><div className='ml-2'>Upload</div></button>
              <button className="rounded rounded-sm bg-[#00ADEF] w-40 max-sm:w-20 h-9 mr-2 text-white flex justify-center items-center flex-row"><BiFilter/><div className='ml-2'>Filter</div></button>
              <form className='w-3/4 ' >
                <input className="rounded shadow shadow-gray-600 w-full h-9 p-2 mb-4" type="text" placeholder='Search'/>
              </form>
            </div>
            <Table name={true} date={true} select={link} configured={true} MarkingSchemes={data}/>
        </div>
            // <td className='text-lg px-4 max-sm:px-1 h-10 border-y-2 border-x-2 font-medium opacity-60'>{data.subjectCode}-{data.subjectName}-{data.year}</td>

      ): ( 
        <DragDrop closeFunc={closeModal} data={data}>Marking Scheme</DragDrop>
      )}
      {show && <DragDrop closeFunc={closeModal} data={data}>Marking Scheme</DragDrop>}
    </div>
  )
}

export default MarkingSchemes
