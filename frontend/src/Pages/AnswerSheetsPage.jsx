import NavBar from '../Components/NavBar'
import SideBar from '../Components/SideBar'
import AnswerSheets from '../Components/AnswerSheets/AnswerSheets'
import {useEffect, useState} from 'react'
import {useParams} from 'react-router-dom'
import { MoonLoader } from 'react-spinners';
import axios from 'axios'
function AnswerSheetsPage() {
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

  return (
    <div>
      <NavBar clicked={isClicked}/>
      <SideBar mcq subjects markingSchemes answerPapers onClickFunc={handleClick} clicked={isClicked}/>
      {/* <AnswerSheets clicked={isClicked} data={answerSheet} markingScheme={markingScheme}/> */}
      {isLoading ? <MoonLoader color="#4457FF" height={6} width={128} className='absolute top-[20vw] left-[55%]'/> 
        :<AnswerSheets clicked={isClicked} data={answerSheet} markingScheme={markingScheme}/>
      }
    </div>
  )
}

export default AnswerSheetsPage
