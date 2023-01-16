from django.shortcuts import render

# Create your views here.
function HomeTab() {
  const [visible, setVisible] = useState(false);

  return (
    
          <Tab visible={visible} className="className" title="Why do it">
            <p className="mb-4">Why do it</p>
            <p className="mb-4">
              {" "}
              Have fun connecting & sharing, or promote yourself or business
              through your very own box-in-the-world. Hit the Get a box button
              on the map to get started.
            </p>
          </Tab>
          <Tab visible={visible} className="className" title="How it works">
            <p className="mb-4">How it works</p>
            <p className="mb-4">
              {" "}
              Have fun connecting & sharing, or promote yourself or business
              through your very own box-in-the-world. Hit the Get a box button
              on the map to get started.
            </p>
          </Tab>
        </Tabs>
      </FadeInOut>
    </div>
  );
}

export default HomeTab;