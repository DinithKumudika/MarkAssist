import MarksBox from "./MarksBox"
import Button from "../Button"
import classnames from 'classnames';
import { useState } from 'react'
function Marks({clicked,answers,markings}) {
  const classes = classnames('sidebar static max-sm:ml-16 pt-[80px]');
  // const answersheets = JSON.parse(localStorage.getItem('answers'));
  // const markingschemes = JSON.parse(localStorage.getItem('markingSceme'));
  // console.log(answers)
  // console.log(markings)
  const [showImages, setShowImages] = useState(false);
  const handleIconClick = () => {
    setShowImages((prev) => !prev);
  };

  const data = answers.map((answer, index) => (
      <MarksBox
        key={answer.id}
        markingScheme_URL={markings[index].uploadUrl}
        answersheet_URL={answer.uploadUrl}
        answer={answer}
        marking={markings[index]}
        showImages={showImages}
      />
      // console.log(markings[index])
    ));

  return (
    <div className={`${classes} ${clicked === 'outer' ? ' ml-16 outer w-[calc(100vw-64px)]' : 'ml-64 w-[calc(100vw-256px)] inner'} max-sm:16 max-sm:w-[calc(100vw-64px)]`}>
      <p className="text-center text-[#191854] text-xl font-bold">Marking Scheme</p>
      <p className="text-center font-medium">Check your marking scheme and deselect the unnecessary selections</p>
      {/* <button onClick={handleIconClick}>View All</button> */}
      {
        showImages ? <Button onClick={handleIconClick} classNames="w-24 text-center bg-custom-blue-2 absolute left-[85%] mt-2">Hide All</Button>
        : <Button onClick={handleIconClick} classNames="w-24 text-center bg-custom-blue-2 absolute left-[85%] mt-2">View All</Button>
      }
      {data}
    </div>
  )
}

export default Marks
