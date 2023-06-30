function MarksBox() {
  const markingScheme_URL= "https://firebasestorage.googleapis.com/v0/b/papermarkin.appspot.com/o/uploads%2Fpdf%2F7a48e8d4-fd37-42ab-82a6-8ff1d5402cf5_cropped_2-1.jpg.jpg?alt=media"
  const answersheet_URL =  "https://firebasestorage.googleapis.com/v0/b/papermarkin.appspot.com/o/uploads%2Fpdf%2F633d6cde-f9a8-4892-a1d1-9573d4ce52cd_cropped_2-2.jpg.jpg?alt=media"
  return (
    <div className="flex flex-col my-6 p-6">
      <p className="font-bold mb-1">Q1</p>
      <div className="bg-[#D4D4D4] rounded rounded-xl">
        <div className="flex flex-row h-max  px-2 rounded rounded-xl p-4 max-md:flex-col">
          <div className=" basis-6/12 mr-1 text-center max-md:mr-0 max-md:mb-2">
            <p className="text-xl text-[#191854] text-center font-bold my-2">Marking Scheme</p>
            <img  className="w-full h-fit " src={markingScheme_URL} alt="Marking scheme photo"/>
          </div>
          <div className=" basis-6/12 ml-1 max-md:ml-0 ">
            <p className="text-xl text-[#191854] text-center font-bold my-2">Students answer</p>
            <img  className="w-full h-fit " src={answersheet_URL} alt="Answer photo"/>
          </div>
        </div>
        <div className=" py-4 flex flex-row justify-between px-2 max-md:flex-col max-md:items-center">
          <div  className="bg-[#EDEDED] px-2 rounded rounded-xl w-52 flex flex-row items-center justify-center mb-2 max-md:justify-between max-md:px-4">
            <label className="mr-2">Marks:</label>
            <input type="text" value="100%" className="bg-[#EDEDED] mr-2 h-12 text-center rounded rounded-lg font-bold w-12" disabled/>
          </div>
          <div  className="bg-[#EDEDED] px-2 rounded rounded-xl w-52 flex flex-row items-center justify-center mb-2 max-md:justify-between max-md:px-4">
            <label className="mr-2">OMR Accuracy:</label>
            <input type="text" value="100%" className="bg-[#EDEDED] mr-2 h-12 text-center rounded rounded-lg font-bold w-12" disabled/>
          </div>
          <div className="bg-[#EDEDED] px-2 rounded rounded-xl w-52 flex flex-row items-center justify-center mb-2 max-md:justify-between max-md:px-4">
            <label className="mr-2">OCR Accuracy:</label>
            <input type="text" value="100%" className="bg-[#EDEDED] mr-2 h-12 text-center rounded rounded-lg font-bold w-12" disabled/>
          </div>
        </div>

      </div>
    </div>
  )
}

export default MarksBox