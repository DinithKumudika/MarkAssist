import NavBar from '../Components/NavBar'
import SideBar from '../Components/SideBar'
import AnswerSheets from '../Components/AnswerSheets/AnswerSheets'
import {useEffect, useState} from 'react'
import {useParams} from 'react-router-dom'
import axios from 'axios'
function AnswerSheetsPage() {
  const { year,subjectId} = useParams()
  const allItems=JSON.parse(localStorage.getItem('tokenData'));
  if(!allItems){
    window.location.href="/";
  }
  const user_id=allItems['user_id'];
  const [isClicked,setClick] = useState("outer");
  const [markingScheme,setMarkingScheme] = useState([]);

  const name=`${subjectId}---- ${year} ---Marking Scheme`

  // useEffect(()=>{
  //   try{
  //     const response = axios.get(`http://localhost:5000/api/answersheets/${year}/${subjectId}/${user_id}`);
  //     const data = response.data;
  //     setMarkingScheme(data);
  //   }catch(error){
  //     console.log(error);
  //   }
  // },[]);

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
      <NavBar />
      <SideBar mcq subjects markingSchemes answerPapers onClickFunc={handleClick} clicked={isClicked}/>
      <AnswerSheets clicked={isClicked} data="hello"/>
      
    </div>
  )
}

export default AnswerSheetsPage
