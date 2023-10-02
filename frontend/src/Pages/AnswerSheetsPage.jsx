import NavBar from '../Components/NavBar'
import SideBar from '../Components/SideBar'
import AnswerSheets from '../Components/AnswerSheets/AnswerSheets'
import {useEffect, useState} from 'react'
import {useLocation, useParams,Link} from 'react-router-dom'
import { MoonLoader } from 'react-spinners';
import axios from 'axios'
import classNames from 'classnames'
function AnswerSheetsPage({page}) {
  const { year,subjectId} = useParams()
  const allItems=JSON.parse(localStorage.getItem('tokenData'));
  if(!allItems){
    window.location.href="/";
  }
  const user_id=allItems['user_id'];
  const [isClicked,setClick] = useState("inner");
  const [answerSheet,setAnswerSheet] = useState([]);
  const [markingScheme, setMarkingScheme] = useState()
  const [isLoading, setIsLoading] = useState(true);
  const name=`${subjectId}---- ${year} ---Marking Scheme`
  const classes = classNames('sidebar static max-sm:ml-16 pt-[52px]');
  const location = useLocation();
  let currentPath = location.pathname.split('/')?.[1];
  console.log("currentPath:",currentPath);


  useEffect(()=>{
    axios
    .get(`http://127.0.0.1:8000/api_v1/markings/${subjectId}`)
    .then((response)=>{
      console.log("Markingscheme:",response.data);
      setMarkingScheme(response.data);
      // setIsLoading(false);
      axios
      .get(`http://127.0.0.1:8000/api_v1/papers/subjects/${subjectId}`)
      .then((response)=>{
        console.log(response.data);
        setAnswerSheet(response.data);
        setIsLoading(false);
      })
      .catch((error)=>{
        console.log(error);
        setAnswerSheet(null)
        setIsLoading(false);
      })
    })
    .catch((error)=>{
      console.log(error);
      setMarkingScheme(null)
      setIsLoading(false);
    })
  },[]);

  // //Function to handle the click of the hamburger menu
  const handleClick = () => {
    if(isClicked==="outer"){
    setClick("inner")
    }else{
    setClick("outer")
    }
  }

  function linkClasses(type=null){
    console.log("type:",type);
    let classes = 'shadow shadow-gray-500 font-bold flex flex-row justify-center items-center h-12 w-full text-center ';
    if(type===page){
      classes+= ' bg-gray-400 ';
    }else{
      classes+=' bg-gray-200 '
    }
    return classes;
  }

  return (
    <div>
      <NavBar clicked={isClicked}/>
      <SideBar mcq subjects markingSchemes answerPapers onClickFunc={handleClick} clicked={isClicked}/>
      {/* <AnswerSheets clicked={isClicked} data={answerSheet} markingScheme={markingScheme}/> */}
      {isLoading ? <MoonLoader color="#4457FF" height={6} width={128} className='absolute top-[20vw] left-[55%]'/> 
        :
        <div className={`${classes} ${isClicked === 'outer' ? ' ml-16 outer w-[calc(100vw-64px)]' : 'ml-64 w-[calc(100vw-256px)] inner'} max-sm:16 max-sm:w-[calc(100vw-64px)]`}>
          <div className='flex flex-row justify-between items-center h-12'>
            <Link className={`${linkClasses('answersheets')} `} to={`/answersheets/${year}/${subjectId}`}>
              <div>
                Answer Sheets
              </div>
            </Link>
            <Link className={`${linkClasses('assignments')} `} to={`/assignments/${year}/${subjectId}`}>
              <div>
                Assignment Marks
              </div>
            </Link>
            <Link className={`${linkClasses('nonocr')} `} to={`/nonocr/${year}/${subjectId}`}>
              <div >
                Non-OCR Marks
              </div>
            </Link>
          </div>
          {
            page==='answersheets' ? (<AnswerSheets page={page} clicked={isClicked} data={answerSheet} markingScheme={markingScheme} year={year} subjectId={subjectId}/>)
            : page==='assignments' ? (<AnswerSheets page={page} clicked={isClicked} data={answerSheet} markingScheme={markingScheme} year={year} subjectId={subjectId}/>)
            : (<AnswerSheets page={page} clicked={isClicked} data={answerSheet} markingScheme={markingScheme} year={year} subjectId={subjectId}/>)
          }
          
        </div>
      }
    </div>
  )
}

export default AnswerSheetsPage
