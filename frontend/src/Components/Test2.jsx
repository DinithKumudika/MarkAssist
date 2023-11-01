import { PencilIcon } from "@heroicons/react/24/solid";
import { ArrowDownTrayIcon, MagnifyingGlassIcon } from "@heroicons/react/24/outline";
import {
  Card,
  CardHeader,
  Typography,
  Button,
  CardBody,
  Chip,
  CardFooter,
  Avatar,
  IconButton,
  Tooltip,
  Input,
} from "@material-tailwind/react";
import Filter from '../Components/Filter'
 
const TABLE_HEAD = ["Transaction", "Amount", "Date", "Status", "Account", ""];
 
const TABLE_ROWS = [
  {
    img: "/img/logos/logo-spotify.svg",
    name: "Spotify",
    amount: "$2,500",
    date: "Wed 3:00pm",
    status: "paid",
    account: "visa",
    accountNumber: "1234",
    expiry: "06/2026",
  },
  {
    img: "/img/logos/logo-amazon.svg",
    name: "Amazon",
    amount: "$5,000",
    date: "Wed 1:00pm",
    status: "paid",
    account: "master-card",
    accountNumber: "1234",
    expiry: "06/2026",
  },
  {
    img: "/img/logos/logo-pinterest.svg",
    name: "Pinterest",
    amount: "$3,400",
    date: "Mon 7:40pm",
    status: "pending",
    account: "master-card",
    accountNumber: "1234",
    expiry: "06/2026",
  },
  {
    img: "/img/logos/logo-google.svg",
    name: "Google",
    amount: "$1,000",
    date: "Wed 5:00pm",
    status: "paid",
    account: "visa",
    accountNumber: "1234",
    expiry: "06/2026",
  },
  {
    img: "/img/logos/logo-netflix.svg",
    name: "netflix",
    amount: "$14,000",
    date: "Wed 3:30am",
    status: "cancelled",
    account: "visa",
    accountNumber: "1234",
    expiry: "06/2026",
  },
];
 
export default function Example() {
  return (
    <div className="w-5/6 gap-5 pt-0 pb-0 pl-4 pr-4 mt-8 mb-2 ml-40 y-full">
    <Card className="object-right-top w-full h-1/4">
      <CardHeader floated={false} shadow={false} className="rounded-none">
        <div className="flex flex-col justify-between gap-8 mt-2 mb-2 md:flex-row md:items-center">
          <div className="flex flex-row gap-8">
            <Typography variant="h5" color="blue-gray">
            Count (7)
            </Typography>
            
            <Typography color="gray" className="mt-1 font-normal">
               {<Filter />}
            </Typography>
          </div>
          <div className="flex w-full gap-6 shrink-0 md:w-max">
            <div className="w-full ml-2 md:w-72">
              <Input  icon={<MagnifyingGlassIcon className="w-5 h-5 mt-2" />} />
            </div>
            <Button className="flex items-center w-auto h-10 gap-0 font-bold text-white bg-blue-500 hover:bg-blue-700" color="blue" size="sm">
            <svg class="h-8 w-8 text-white"  width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">  <path stroke="none" d="M0 0h24v24H0z"/>  <line x1="12" y1="5" x2="12" y2="19" />  <line x1="5" y1="12" x2="19" y2="12" /></svg> Add Person 
            </Button>
          </div>
        </div>
      </CardHeader>
      
    </Card>
    </div>
  );
}