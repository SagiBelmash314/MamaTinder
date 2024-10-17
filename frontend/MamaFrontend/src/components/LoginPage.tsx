import { Button, IconButton, TextField } from "@mui/material";
import Banner from "./Banner";
import Tag from "./Tag";
import { useState } from "react";
import UploadPhotoBtn from "./UploadPhotoBtn";
import Grid from "./Grid";
import { ArrowForward } from "@mui/icons-material";

const LoginPage = () => {
  const [isExpandad, setIsExpanded] = useState(false);

  const login = (
    <>
      <h1 className="bold mb-5 text-3xl">Welcome to MamaTinder!</h1>
      <TextField placeholder="Username" className="" />
      <TextField placeholder="Password" />
      <Button color="secondary" variant="contained" className="w-40 ">
        Log in
      </Button>
      <Button onClick={() => expand()}>Not registered? Click here!</Button>
    </>
  );

  const register = (
    <div className="flex flex-col h-full">
      {/* The upper bar */}
      <div className="flex items-center justify-between w-full">
        <div className="flex items-center">
          <img
            src="https://t4.ftcdn.net/jpg/02/66/72/41/360_F_266724172_Iy8gdKgMa7XmrhYYxLCxyhx6J7070Pr8.jpg"
            className="z-20 h-20 w-20 p-2 rounded-full"
          />
          <h1 className="ml-4 text-3xl bold">MamaTinder</h1>
        </div>
        <div className="mr-4">
          <IconButton onClick={() => shrink()} size={"large"}>
            <ArrowForward fontSize="large" />
          </IconButton>
        </div>
      </div>
      {/* The credentials */}
      <div className="z-20 flex justify-left items-center w-full flex-grow">
        <UploadPhotoBtn className="w-48 h-full ml-2 mr-3" />
        {/* First credentials */}
        <Grid columns={2} width={400}>
          <h1>Username:</h1>
          <TextField />
          <h1>Password:</h1>
          <TextField />
          <h1>Re-enter Password:</h1>
          <TextField />
          <h1>Birth date:</h1>
          <TextField />
        </Grid>
      </div>

      {/* Bottom Bar */}
      <div className="h-12 w-full p-2 bg-blue-300 rounded-b">
        <div className="flex rounded-full h-full w-full bg-white justify-center items-center">
          <h1>
            <b>Pay attention!</b> After you register the credentials (except the
            photos) cannot be changed
          </h1>
        </div>
      </div>
    </div>
  );

  const [tagContent, setTagContent] = useState(login);

  const expand = () => {
    setIsExpanded(true);
    setTimeout(() => {
      setTagContent(register);
    }, 600);
  };

  const shrink = () => {
    setIsExpanded(false);
    setTimeout(() => {
      setTagContent(login);
    }, 600);
  };

  return (
    <>
      <Banner height={"10px"} />
      <div className="flex flex-col items-center bg-green-700 justify-center h-screen w-screen">
        <Tag isExpanded={isExpandad}>{tagContent}</Tag>
      </div>
    </>
  );
};

export default LoginPage;
