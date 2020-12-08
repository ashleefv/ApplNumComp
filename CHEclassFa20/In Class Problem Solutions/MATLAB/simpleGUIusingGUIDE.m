function varargout = simpleGUIusingGUIDE(varargin)
% SIMPLEGUIUSINGGUIDE MATLAB code for simpleGUIusingGUIDE.fig
%      SIMPLEGUIUSINGGUIDE, by itself, creates a new SIMPLEGUIUSINGGUIDE or raises the existing
%      singleton*.
%
%      H = SIMPLEGUIUSINGGUIDE returns the handle to a new SIMPLEGUIUSINGGUIDE or the handle to
%      the existing singleton*.
%
%      SIMPLEGUIUSINGGUIDE('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in SIMPLEGUIUSINGGUIDE.M with the given input arguments.
%
%      SIMPLEGUIUSINGGUIDE('Property','Value',...) creates a new SIMPLEGUIUSINGGUIDE or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before simpleGUIusingGUIDE_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to simpleGUIusingGUIDE_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help simpleGUIusingGUIDE

% Last Modified by GUIDE v2.5 14-Oct-2020 08:52:53

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @simpleGUIusingGUIDE_OpeningFcn, ...
                   'gui_OutputFcn',  @simpleGUIusingGUIDE_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before simpleGUIusingGUIDE is made visible.
function simpleGUIusingGUIDE_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to simpleGUIusingGUIDE (see VARARGIN)
% Create the data to plot.
handles.peaks=peaks(35);
handles.membrane=membrane;
[x,y] = meshgrid(-8:.5:8);
r = sqrt(x.^2+y.^2) + eps;
sinc = sin(r)./r;
handles.sinc = sinc;
% Set the current data value.
handles.current_data = handles.peaks;
surf(handles.current_data)

% Choose default command line output for simpleGUIusingGUIDE
handles.output = hObject;

% Update handles structure
% THIS IS HOW YOU SAVE AT THE END OF ANY GUI FUNCTION
guidata(hObject, handles);

% UIWAIT makes simpleGUIusingGUIDE wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = simpleGUIusingGUIDE_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on button press in mesh_button.
function mesh_button_Callback(hObject, eventdata, handles)
% hObject    handle to mesh_button (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Display mesh plot of the currently selected data.
  mesh(handles.current_data);

% --- Executes on button press in surf_button.
function surf_button_Callback(hObject, eventdata, handles)
% hObject    handle to surf_button (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Display surf plot of the currently selected data.
surf(handles.current_data);

% --- Executes on button press in contour_button.
function contour_button_Callback(hObject, eventdata, handles)
% hObject    handle to contour_button (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Display mesh plot of the currently selected data.
  contour(handles.current_data);

% --- Executes on selection change in popupmenu1.
function popupmenu1_Callback(hObject, eventdata, handles)
% hObject    handle to popupmenu1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = cellstr(get(hObject,'String')) returns popupmenu1 contents as cell array
%        contents{get(hObject,'Value')} returns selected item from popupmenu1

% Determine the selected data set.
str = get(hObject, 'String');
val = get(hObject,'Value');
% Set current data to the selected data set.
if strcmp(str{val}, 'peaks')
    % User selects peaks.
   handles.current_data = handles.peaks;
elseif strcmp(str{val}, 'membrane' )
    % User selects membrane.
   handles.current_data = handles.membrane;
elseif strcmp(str{val}, 'sinc' )
    % User selects sinc.
   handles.current_data = handles.sinc;
end
% Save the handles structure.
guidata(hObject,handles)

% --- Executes during object creation, after setting all properties.
function popupmenu1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to popupmenu1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
