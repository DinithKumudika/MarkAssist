function SubmitButton({children,type}) {
  return (
    <button className="rounded rounded-sm bg-sky-600 w-full h-9  text-white" type={type}>{children}</button>
  )
}

export default SubmitButton
