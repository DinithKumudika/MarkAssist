import DragDrop from '../DragDrop'
import Table from '../Table'
import classnames from 'classnames'
import { AiOutlinePlus } from "react-icons/ai";
import Modal from '../Modal';
import { BiFilter } from "react-icons/bi";
import { useState,useEffect } from 'react'
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
function AnswerSheets({clicked, data,markingScheme}) {
  const navigate = useNavigate();
  const [markings,setMarkings] = useState([]);
  const [answers,setAnswers] = useState([]);
  const [markingschemeID,setmarkingschemeID] = useState("");
  const [isLoading, setIsLoading] = useState(true);
  const [isLoading2, setIsLoading2] = useState(true);
  const [marks,setMarks] = useState([]);

  const [Checked, setChecked] = useState({})
  const [checkAll, setCheckAll] = useState(false)
  useEffect(()=>{
    data?.map((AnswerSheet) => {
        setChecked(prevState=>{return {...prevState,[AnswerSheet.paper]:false}})
    })
  },[])

  const handleAllCheck = (ev) =>{
    const newCheckAll = {};
    for (const key in Checked){
      if(ev.target.checked){
        newCheckAll[key] = true;
      }else{
        newCheckAll[key] = false;
      }
    }
    setChecked(newCheckAll);
    setCheckAll(ev.target.checked);
    console.log("newCheckAll:",checkAll)
    console.log("newCheck:",Checked)

  }

  const handleCheck = (ev) =>{
    setChecked((prevState) => {
      console.log("prev state:", Checked);
      return { ...prevState, [ev.target.name]: ev.target.checked };
    });
  }


  console.log("DAaaTA:"+markingScheme?.isProceeded)
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

  const handleLink = () =>{
    navigate(`/markingschemes/${markingScheme?.year}/${markingScheme?.subjectId}`)
  }

  const handleGenerateAccuracy= ()=>{
    console.log("data::",data);
    console.log("checked::",Checked);
    // data.forEach((data,index)=>{
      // if(Checked[data.paper]){
        
            axios
            .patch(`http://127.0.0.1:8000/api_v1/answers/compare/${markingScheme.id}/${data[0].subjectId}`,Checked)
            .then((response)=>{
              const marks = response.data
              // setMarkings(marking)
              // markingschemeID = marking[0].markingScheme
              console.log("Markkkkkkssssss:",marks)
    
            })
            .catch((error) => {
              console.error(error);
              // setMarks(null)
              // Handle the error, e.g., display an error message to the user
            });
      // }
    // })
    
    // console.log("Markingsss:",answers)
  }

  return (
    <div className={`${classes} ${clicked === 'outer' ? ' ml-16 outer w-[calc(100vw-64px)]' : 'ml-64 w-[calc(100vw-256px)] inner'} max-sm:16 max-sm:w-[calc(100vw-64px)]`}>
      {data ? (
        <div className=' flex flex-col items-center justify-top w-full h-full px-10 max-sm:px-4 py-8'>
            <div className='mb-12 text-center  w-full'>
              <p className='text-xl font-bold text-[#191854]'>Answer Sheets</p>
              <p className='text-lg text-black opacity-60'>Upload answer papers</p>
            </div>
            <div className=' max-sm:px-4 flex flex-col lg:flex-row justify-between w-full md:flex-col'>
              <div className='flex lg:w-1/2 mb-2  md:[90%] md:mb-2 md-max:justify-between'>
                <button className="rounded rounded-sm bg-custom-blue-main w-fit px-2 max-sm:w-20 h-9 mr-2 text-white flex justify-center items-center flex-row" onClick={handleCKick}><AiOutlinePlus/><div className='ml-2'>Upload</div></button>
                <button className="rounded rounded-sm bg-custom-blue-main w-fit px-2 max-sm:w-20 h-9 mr-2 text-white flex justify-center items-center flex-row"><BiFilter/><div className='ml-2'>Filter</div></button>
                <button className="rounded rounded-sm w-fit bg-custom-blue-main max-sm:w-fill px-2 h-9 mr-2 text-white flex justify-center items-center flex-row" onClick={handleGenerateAccuracy}><BiFilter/><div className='ml-2'>Generate Accuracy</div></button>
              </div>
              <form className='lg:w-1/2 md:2/3 ' >
                <input className="rounded shadow shadow-gray-600 w-full h-9 p-2 mb-4" type="text" placeholder='Search'/>
              </form>
            </div>
            <Table check={true} checked={true} Checked={Checked} checkAll={checkAll} name={true} handleCheck={handleCheck} handleAllCheck={handleAllCheck} date={true} select={true} AnswerSheets={data}/>
        </div>
      ): ( 
        <DragDrop closeFunc={closeModal}>Answer Sheets</DragDrop>
      )}
        {!markingScheme?.isProceeded ? <Modal handleLink={handleLink} message="Configure the marking scheme before uploading answer sheets."/> : show && <DragDrop closeFunc={closeModal}>Answer Sheets</DragDrop>}
       {/* {(markingScheme?.isProceeded && <Modal handleLink={handleLink} message="Configure the marking scheme before uploading answer sheets."/>) && show && <DragDrop closeFunc={closeModal}>Answer Sheets</DragDrop>} */}
    </div>
  )
}

export default AnswerSheets
