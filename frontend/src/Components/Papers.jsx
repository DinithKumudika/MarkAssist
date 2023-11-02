import classnames from "classnames";
import Table from "./Table";
function Papers({clicked}) {
  const classes = classnames('sidebar static max-sm:ml-16 pt-[80px] px-4');

  const data = [
    {
      "index":20001711,
      "marks":80,
      "grading": "A+"
    },
    {
      "index":20001472,
      "marks":50,
      "grading": "B-"
    },
    {
      "index":20205352,
      "marks":74,
      "grading": "A"
    },
    {
      "index":20202417,
      "marks":23,
      "grading": "E"
    },
    {
      "index":20001738,
      "marks":95,
      "grading": "A+"
    },
  ]
  return (
    <div className={`${classes} ${clicked === 'outer' ? 'ml-16 outer' : 'ml-64 inner'}`}>
      <p className="text-center text-[#191854] text-xl font-bold mb-4">Marks</p>
      {/* <p className="text-center font-medium">Check your marking scheme and deselect the unnecessary selections</p> */}
      <Table index={true} overallMark={true} grade={true} grades={data}/>
    </div>
  )
}

export default Papers
