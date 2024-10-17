import { ReactNode, useEffect, useState } from "react";

interface Props {
  children: ReactNode;
  isExpanded: boolean;
}

const Tag = ({ children, isExpanded }: Props) => {
  const [w, setW] = useState(500);
  const [h, setH] = useState(300);
  const [className, setClassName] = useState(
    "flex flex-col bg-white items-center justify-center"
  );

  const [opacity, setOpacity] = useState(1);

  const [loaded, setLoaded] = useState(false);

  const shrink = () => {
    setW(500);
    setOpacity(0);
    const firstTimeoutId = setTimeout(() => {
      setH(300);
      const secondTimeoutId = setTimeout(() => {
        setClassName("flex flex-col bg-white items-center justify-center");
        setOpacity(1);
        clearTimeout(secondTimeoutId);
      }, 500);
      clearTimeout(firstTimeoutId);
    }, 500);
  };

  const expand = () => {
    setH(400);
    setOpacity(0);
    const firstTimeoutId = setTimeout(() => {
      setW(634);
      const secondTimeoutId = setTimeout(() => {
        setClassName("bg-blue-200");
        setOpacity(1);
        clearTimeout(secondTimeoutId);
      }, 500);
      clearTimeout(firstTimeoutId);
    }, 500);
  };

  useEffect(() => {
    if (loaded) {
      isExpanded ? expand() : shrink();
    } else {
      setLoaded(true);
    }
  }, [isExpanded]);

  return (
    <>
      <div
        className={"rounded mt-40 z-10 " + className}
        style={{
          width: `${w}px`,
          height: `${h}px`,
          opacity: `${opacity}`,
          transition: "width 0.5s ease, height 0.5s ease, opacity 0.4s ease",
        }}
      >
        {children}
      </div>
      <div
        className={"rounded mt-40 absolute bg-white z-0"}
        style={{
          width: `${w}px`,
          height: `${h}px`,
          transition: "width 0.5s ease, height 0.5s ease",
        }}
      />
    </>
  );
};

export default Tag;
