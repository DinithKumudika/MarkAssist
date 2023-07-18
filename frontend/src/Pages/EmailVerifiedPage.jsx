import { MdVerified } from "react-icons/md";
import Button from "../Components/Button";
function EmailVerifiedPage() {
  const handleClick = ()=>{
    window.location.href = '/';
  }
  return (
    <div className="border-2 border-gray-900 flex items-center justify-center h-full">
      <div className="flex flex-col border-2 items-center justify-center shadow shadow-gray-300 h-full w-[500px] max-md:w-[400px] px-8">
        <MdVerified className="text-8xl m-4 text-green-500"/>
        <h1 className="text-4xl m-4">Email Verified</h1>
        <p className="text-center">Your email was verified. You can continue suing the application.</p>
        <Button classNames="bg-green-500 mt-4" onClick={handleClick}>Continue to Login</Button>
      </div>
    </div>
  )
}

export default EmailVerifiedPage
