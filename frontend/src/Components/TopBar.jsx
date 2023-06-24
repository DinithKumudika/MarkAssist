import { Fragment } from 'react'
import { Disclosure, Menu, Transition } from '@headlessui/react'
import { Bars3Icon, BellIcon, XMarkIcon } from '@heroicons/react/24/outline'

const navigation = [
  { name: 'Questions', href: '#', current: true },
  { name: 'Essay', href: '#', current: false },
  { name: 'MCQ', href: '#', current: false },
  { name: 'Log in', href: '#', current: false },
  { name: 'Get Started', href: '#', current: false },
]
// hi
function classNames(...classes) {
  return classes.filter(Boolean).join(' ')
}

export default function TopBar() {
  return (
    <Disclosure as="nav" className="#F5F5F5;">
      {({ open }) => (
        <>
          <div className="px-2 mx-auto max-w-7xl sm:px-6 lg:px-8">
            <div className="relative flex items-center justify-between h-16">
              <div className="absolute inset-y-0 left-0 flex items-center sm:hidden">
                {/* Mobile menu button*/}
                <Disclosure.Button className="inline-flex items-center justify-center p-2 text-gray-400 rounded-md hover:bg-gray-700 hover:text-white focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white">
                  <span className="sr-only">Open main menu</span>
                  {open ? (
                    <XMarkIcon className="block w-6 h-6" aria-hidden="true" />
                  ) : (
                    <Bars3Icon className="block w-6 h-6" aria-hidden="true" />
                  )}
                </Disclosure.Button>
              </div>
              <div className="flex items-center justify-center flex-1 sm:items-stretch sm:justify-start">
                <div className="flex items-center flex-shrink-0">
                  <img
                    className="block w-auto h-8 lg:hidden"
                    src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=500"
                    alt="Your Company"
                  />
                  <img
                    className="hidden w-auto h-8 lg:block"
                    src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=500"
                    alt="Your Company"
                  />
                </div>
                <div className="hidden sm:ml-6 sm:block">
                  <div className="flex space-x-4">
                    {navigation.map((item) => (
                      <a
                        key={item.name}
                        href={item.href}
                        className={classNames(
                          item.current ? 'bg-#f8fafc text-blue-500' : 'text-gray-300 hover:bg-gray-700 hover:text-white',
                          'rounded-md px-3 py-2 text-sm font-medium'
                        )}
                        aria-current={item.current ? 'page' : undefined}
                      >
                        {item.name}
                      </a>
                    ))}
                  </div>
                </div>
              </div>
              
            </div>
          </div>

          <Disclosure.Panel className="sm:hidden">
            <div className="px-2 pt-2 pb-3 space-y-1">
              {navigation.map((item) => (
                <Disclosure.Button
                  key={item.name}
                  as="a"
                  href={item.href}
                  className={classNames(
                    item.current ? 'bg-gray-900 text-white' : 'text-gray-300 hover:bg-gray-700 hover:text-white',
                    'block rounded-md px-3 py-2 text-base font-medium'
                  )}
                  aria-current={item.current ? 'page' : undefined}
                >
                  {item.name}
                </Disclosure.Button>
              ))}
            </div>
          </Disclosure.Panel>
        </>
      )}
    </Disclosure>
  )
}


// import React from 'react'
// import './TopBar.css';
// import { Link } from 'react-router-dom';

// function TopBar() {
//   return (
//     <div>
//       <div className="nav">
//       <Link to="/" className='topbar-link1'>
//         Questions
//         </Link> 
//         <Link to="essayPage" className='topbar-link2'>
//         Essay
//         </Link>
//         <Link to="mcqPage" className='topbar-link3'>
//         MCQ
//         </Link> 
//         <Link to="loginPage" className='topbar-link4'>
//         Log in
//         </Link>
//         <Link to="mcqPage" className='topbar-link5'>
//         Get Started
//         <img
//         src="./photos/🦆 icon _arrow right.png"
//         alt="arrow"
//         className="arrow-icon"></img>
//         </Link> 
//         <div>
//             <img
//             src="./photos/Vector 1.png"
//             alt="vector1"
//             className='vector1-image'></img> 
//             <img
//             src="./photos/logo.png"
//             alt="logo"
//             className="logo-image"></img>
//         </div>
//         </div>
//     </div>
    
//   )
// }

// export default TopBar


