import * as React from 'react';
import Box from '@mui/joy/Box';
import Textarea from '@mui/joy/Textarea';

const LargeTextBox = ({ }, ref: any) => {
  const [italic, setItalic] = React.useState(false);
  const [fontWeight, setFontWeight] = React.useState('normal');
  
  return (
      <Textarea
        slotProps={{ textarea: { ref: ref } }}
        placeholder="Study Notes"
        minRows={3}
        endDecorator={
          <Box
            sx={{
              display: 'flex',
              gap: 'var(--Textarea-paddingBlock)',
              pt: 'var(--Textarea-paddingBlock)',
              borderTop: '1px solid',
              borderColor: 'divider',
              flex: 'auto',
            }}
          >
          </Box>
        }
        sx={{
          minWidth: 300,
          fontWeight,
          fontStyle: italic ? 'italic' : 'initial',
          background : "#23272f",
          color: "#ebecf0",
          marginTop: "1vh"
        }}
      />
  );
}

export default React.forwardRef(LargeTextBox);
