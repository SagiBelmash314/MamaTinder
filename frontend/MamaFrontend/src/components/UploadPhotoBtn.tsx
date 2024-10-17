import { Button, styled } from "@mui/material";

interface Props {
  className: string;
}

const UploadPhotoBtn = ({ className }: Props) => {
  const VisuallyHiddenInput = styled("input")({
    clip: "rect(0 0 0 0)",
    clipPath: "inset(50%)",
    height: 1,
    overflow: "hidden",
    position: "absolute",
    bottom: 0,
    left: 0,
    whiteSpace: "nowrap",
    width: 1,
  });
  return (
    <div className={className}>
      <Button
        component="label"
        role={undefined}
        variant="contained"
        tabIndex={-1}
        sx={{
          borderRadius: 0,
          boxShadow: "none",
          "&:hover": {
            boxShadow: "none", // Remove shadow on hover
          },
        }}
        style={{ height: "100%", width: "100%" }}
      >
        Upload files
        <VisuallyHiddenInput
          type="file"
          onChange={(event) => console.log(event.target.files)}
          multiple
          accept="image/*"
        />
      </Button>
    </div>
  );
};

export default UploadPhotoBtn;
