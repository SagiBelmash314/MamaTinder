import { Children, cloneElement, ReactNode } from "react";

interface Props {
  columns?: number;
  children?: ReactNode;
  width?: number;
}

const Grid = ({ columns = 1, width = 100, children }: Props) => {
  columns < 1 && (columns = 1);
  const prec = 100 / columns;
  const style: { container: React.CSSProperties; item: React.CSSProperties } = {
    container: {
      width: `${width}px`,
      display: "flex",
      flexWrap: "wrap",
      alignItems: "center",
    },
    item: {
      flex: `0 0 ${prec}%`,
      textAlign: "left",
    },
  };

  const { container, item } = style;

  return (
    <div style={container}>
      {/* For every tag in "children" give the style "item" */}
      {Children.map(children, (child) =>
        cloneElement(child as React.ReactElement, { style: item })
      )}
    </div>
  );
};

export default Grid;
