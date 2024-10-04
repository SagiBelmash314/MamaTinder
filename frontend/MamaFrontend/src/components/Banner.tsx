interface Props {
  height: string;
}

const Banner = ({ height }: Props) => {
  return (
    <div
      className="absolute flex items-center justify-center w-screen"
      style={{ top: `${height}` }}
    >
      <div className="absolute z-10 w-full bg-purple-800 h-40 shadow-[0_10px_30px_rgba(0,0,0,0.5)]" />
      <img
        src="https://t4.ftcdn.net/jpg/02/66/72/41/360_F_266724172_Iy8gdKgMa7XmrhYYxLCxyhx6J7070Pr8.jpg"
        className="z-20 h-44 w-44 rounded-full shadow-[0_10px_30px_rgba(0,0,0,0.5)]"
      />
    </div>
  );
};

export default Banner;
